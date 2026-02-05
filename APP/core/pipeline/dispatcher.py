class Dispatcher:
    def __init__(self, registry, system_schema, input_pipeline, feature_config):
        self.registry = registry
        self.system_schema = system_schema
        self.input_pipeline = input_pipeline
        self.feature_config = feature_config
        self.ipt_handlers = self.registry.input_handlers()
        self.sys_handlers = self.registry.system_handlers()
        self.exe_handlers = self.registry.execute_handlers()

    # ---------------- INPUT ----------------
    def execute_input(self, config, feature):
        res = DSPResult(stage="INPUT", feature=feature)

        if not config:
            return res.fail({"type": "CONFIG_ERROR", "reason": "FEATURE_NOT_DEFINED"})

        if config.get("requires_input") not in {"user", "mixed"}:
            return res.fail({"type": "DISPATCH_ERROR", "reason": "INPUT_NOT_REQUIRED"})

        handlers = self.ipt_handlers
        if feature not in handlers:
            return res.fail({"type": "REGISTRY_ERROR", "reason": "INPUT_HANDLER_NOT_FOUND"})

        try:
            res.payload["input"] = handlers[feature]()
            return res.success()
        except Exception as e:
            return res.fail({"type": "INPUT_ERROR", "reason": str(e)})

    # ---------------- PIPELINE ----------------
    def execute_pipeline(self, config, data, feature):
        res = DSPResult(stage="NORMALIZE", feature=feature)

        pipeline = self.input_pipeline
        result = pipeline.dsp_pipeline(
            data,
            config.get("schema", {}),
        )

        if result["errors"]:
            return res.fail({
                "type": "VALIDATION_ERROR",
                "reason": "Input validation failed",
                "details": result["errors"]
            })

        res.payload["normalized"] = result["correct_data"]
        return res.success()

    # ---------------- SYSTEM DATA ----------------
    def execute_system_data(self, config, feature, data):
        res = DSPResult(stage="SYSTEM_DATA", feature=feature)

        if not config.get("requires_system"):
            return res.fail({"type": "DISPATCH_ERROR", "reason": "SYSTEM_DATA_NOT_REQUIRED"})

        handlers = self.sys_handlers
        if feature not in handlers:
            return res.fail({"type": "REGISTRY_ERROR", "reason": "SYSTEM_HANDLER_NOT_FOUND"})

        try:
            result = self._wrap_result(
                handlers[feature](data)
                if config.get("system_depends_on_input")
                else handlers[feature]()
            )
            
            if not result.get("error"):
                res.payload["system"] = result
                return res.success()
            return res.fail({"type": "HANDLER_ERROR", "reason": result["error"]})
        
        except Exception as e:
            return res.fail({"type": "SYSTEM_ERROR", "reason": str(e)})

    # ---------------- EXECUTE FEATURE ----------------
    def execute_feat(self, config, feature, payload):
        res = DSPResult(stage="EXECUTE", feature=feature)

        handlers = self.exe_handlers
        if feature not in handlers:
            return res.fail({"type": "REGISTRY_ERROR", "reason": "EXECUTE_HANDLER_NOT_FOUND"})

        try:
            res.payload["result"] = handlers[feature](payload) if config.get("execute_accepts_payload") else handlers[feature]()
            return res.success()
        except Exception as e:
            return res.fail({"type": "EXECUTE_ERROR", "reason": str(e)})

    # ---------------- FINAL ----------------
    def execute(self, feature):
        enum_feat, config = self.feature_config.resolve(feature)
        res = DSPResult(stage="FINAL_EXECUTE", feature=enum_feat)

        if not config:
            return res.fail({"type": "CONFIG_ERROR", "reason": "FEATURE_NOT_DEFINED"})

        current_data = None

        # INPUT
        if config.get("requires_input"):
            inp = self.execute_input(config, enum_feat)
            if not inp.ok:
                return inp
            current_data = inp.payload["input"]
            res.payload["input"] = current_data

        # PIPELINE
        if config.get("use_pipeline"):
            pipe = self.execute_pipeline(config, current_data, enum_feat)
            if not pipe.ok:
                return pipe
            current_data = pipe.payload["normalized"]
            res.payload["normalized"] = current_data

        # SYSTEM
        if config.get("requires_system"):
            sysd = self.execute_system_data(config, enum_feat, current_data)
            if not sysd.ok:
                return sysd
            current_data = sysd.payload["system"]
            res.payload["system"] = current_data

        # EXECUTE
        exe = self.execute_feat(config, enum_feat, current_data)
        if not exe.ok:
            return exe

        res.payload["result"] = exe.payload["result"]
        return res.success()

    def _wrap_result(self, result):
        """
        Simplifies the handler result for DSP usage.
        - If there is an error or success is False, returns a dict with the error.
        - Otherwise, returns a dict with the data.
        """
        if not result.ok or result.error:
            return {"error": result.error}
        
        return {"payload": result.payload, "meta": result.meta}

class DSPResult:
    def __init__(self, stage, feature):
        self.ok = False
        self.stage = stage
        self.feature = feature
        self.payload = {
            "input": None,
            "normalized": None,
            "system": None,
            "result": None
        }
        self.error = None

    def fail(self, raw_error):
        self.ok = False
        self.error = wrap_error(self.stage, self.feature, raw_error)
        return self

    def success(self):
        self.ok = True
        return self

def wrap_error(stage, feature, error):
    return {
        "code": error.get("type", "UNKNOWN_ERROR"),
        "message": error.get("reason", "Execution failed"),
        "details": {
            "stage": stage,
            "feature": feature,
            "info": error.get("details", None)
        }
    }

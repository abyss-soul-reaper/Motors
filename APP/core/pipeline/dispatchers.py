class Dispatcher:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl
        
    def dsp_feat_input(self, feature):
        execution_result = {"ok": False,"payload": None,"error": None,"stage": "INPUT"}
        config = self.sys_ctrl.config

        # 1) feature مش موجود في config
        if feature not in config:
            execution_result["error"] = {"type": "CONFIG_ERROR", "reason": "FEATURE_NOT_DEFINED", "feature": feature}
            return execution_result

        requires_input = config[feature].get("requires_input")

        # 2) feature لا يتطلب input
        if requires_input not in {"user", "mixed"}:
            execution_result["error"] = {"type": "DISPATCH_ERROR", "reason": "INPUT_NOT_REQUIRED", "feature": feature}
            return execution_result

        # 3) جلب input handlers
        input_map = self.sys_ctrl.Registry.input_handlers()
        if feature not in input_map:
            execution_result["error"] = {"type": "REGISTRY_ERROR", "reason": "INPUT_HANDLER_NOT_FOUND", "feature": feature}
            return execution_result

        # 4) تنفيذ input handler
        try:
            payload = input_map[feature]()
        except Exception as e:
            execution_result["error"] = {"type": "INPUT_ERROR", "reason": str(e), "feature": feature}
            return execution_result

        # 5) نجاح
        execution_result["ok"] = True
        execution_result["payload"] = payload
        return execution_result

    def dsp_feat(self, feature, data=None):
        execution_result = {"ok": False,"payload": None,"error": None,"stage": "EXECUTE"}
        config = self.sys_ctrl.config

        if feature not in config:
            execution_result["error"] = {"type": "CONFIG_ERROR", "reason": "FEATURE_NOT_DEFINED", "feature": feature}
            return execution_result
        
        exe_map = self.sys_ctrl.Registry.execute_handlers()
        if feature not in exe_map:
            execution_result["error"] = {"type": "REGISTRY_ERROR", "reason": "EXECUTE_HANDLER_NOT_FOUND", "feature": feature}
            return execution_result
        
        try:
            payload = exe_map[feature](data)
        except Exception as e:
            execution_result["error"] = {"type": "EXECUTE_ERROR", "reason": str(e), "feature": feature}
            return execution_result
        
        execution_result["ok"] = True
        execution_result["payload"] = payload
        return execution_result
















    def dsp_valid(self, field, value):
        validators_map = self.sys_ctrl.registry.register_validators()

        if field not in validators_map:
            return False

        return validators_map[field](value)

    def dsp_normalize(self, field, value):
        normalizers_map = self.sys_ctrl.registry.register_normalizers()

        if field not in normalizers_map:
            return value

        return normalizers_map[field](value)

    def execute(self, feature):
        config = self.sys_ctrl.config.get(feature, {})

        if not config.get("requires_input") or config.get("requires_input") == "system":
            raw_data = None
        else:
            raw_data = self.dispatch_feature_input(feature)

        if config.get("use_pipeline"):
            schema = config.get("schema")
            errors, pipeline_result = self.sys_ctrl.pipeline_dsp(
                self.sys_ctrl,
                raw_data,
                schema,
                self.sys_ctrl.sys_schema
            )

            if errors:
                return {"errors": errors}

            data_to_pass = pipeline_result
        else:
            data_to_pass = raw_data

        return self.dispatch_feature(feature, data_to_pass)

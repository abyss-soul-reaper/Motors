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

    def execute_feat(self, feature, data=None):
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
            requires_data = config[feature].get("requires_input")
            if not requires_data:
                payload = exe_map[feature]()
            else:
                payload = exe_map[feature](data)
        except Exception as e:
            execution_result["error"] = {"type": "EXECUTE_ERROR", "reason": str(e), "feature": feature}
            return execution_result
        
        execution_result["ok"] = True
        execution_result["payload"] = payload
        return execution_result

    def execute_input(self, feature):
        execution_result = {"ok": False,"payload": None,"error": None}
        data = self.dsp_feat_input(feature)

        if data["ok"]:
            execution_result["ok"] = True
            execution_result["payload"] = data["payload"]
            return execution_result

        execution_result["error"] = data["error"]
        return execution_result
    
    def execute_pipeline(self, config, data):
        execution_result = {"ok": False,"payload": None,"errors": None, "stage": "NORMALIZE"}
        schema = config.get("schema")
        dsp_pipeline = self.sys_ctrl.dsp_pipeline

        results = dsp_pipeline.dsp_pipeline(
                data, schema, self.sys_ctrl.sys_schema
                )

        if results["errors"]:
            execution_result["errors"] = results["errors"]
            return execution_result
        
        execution_result["ok"] = True
        execution_result["payload"] = results["correct_data"]
        return execution_result

    def execute(self, feature):
        execution_result = {"ok": False,"payload": None,"error": None,"stage": "FINAL_EXECUTE"}
        config = self.sys_ctrl.config.get(feature, {})

        raw_data = None
        if config.get("requires_input") in {"user", "mixed"}:
            result = self.execute_input(feature)
            if not result["ok"]:
                execution_result["error"] = result["error"]
                return execution_result
            raw_data = result["payload"]

        if config.get("use_pipeline"):
            pipe_result = self.execute_pipeline(config, raw_data)
 
            if not pipe_result["ok"]:
                execution_result["error"] =  pipe_result["errors"]
                return execution_result
            data_to_pass = pipe_result["payload"]

        else:
            data_to_pass = raw_data

        final_execute = self.execute_feat(feature, data_to_pass)
        if not final_execute["ok"]:
            execution_result["error"] = final_execute["error"]
            return execution_result
        
        execution_result["ok"] = True
        execution_result["payload"] = final_execute["payload"]
        return execution_result
from APP.core.pipeline.registry import Registry
from APP.core.result.base_result import BaseResult
from APP.core.pipeline.dispatcher import Dispatcher
from APP.core.initializer.initializer import Initializer
from APP.core.pipeline.input_pipeline import InputPipeline

class SystemController:
    """
    Central system controller.
    Holds all system-wide instances, handlers, pipelines, and configuration.
    """

    def __init__(self):
        # ---------------- Build independent components ----------------
        init = Initializer()

        # System State
        self.system_context = init.system_context
        self.permissions = init.permissions

        # Helpers & Utilities
        self.helpers = init.helpers
        self.paginator = init.paginator

        # UI
        self.ui = init.ui

        # Domain Models
        self.user_model = init.user_model

        # Domain Managers
        self.user_manager = init.user_manager
        self.vehicle_manager = init.vehicle_manager

        # Domain Handlers
        self.user_handler = init.user_handler
        self.vehicle_handler = init.vehicle_handler

        # Pipeline Configuration
        self.feature_config = init.feature_config
        self.system_schema = init.system_schema

        # ---------------- Build dependent components ----------------
        # Registry needs access to self (SystemController instance)
        self.registry = Registry(self)

        # InputPipeline needs registry & system_schema
        self.input_pipeline = InputPipeline(self.registry, self.system_schema)

        # Dispatcher needs input_pipeline, registry, feature_config, system_schema
        self.dispatcher = Dispatcher(
            self.registry,
            self.system_schema,
            self.input_pipeline,
            self.feature_config,
        )

    def register_user(self, data):
        res = BaseResult()
        model_result = self.user_model(data).dict_info()
        result = self.user_handler.register(model_result)

        if not result.ok:
            return res.fail(result.error) 

        self.helpers.update_context(self.system_context, result.payload)
        return res.success()
        
    def login_user(self, credentials):
        res = BaseResult()
        result = self.user_handler.login(credentials)

        if not result.ok:
            return res.fail(result.error)

        self.helpers.update_context(self.system_context, result.payload)
        return res.success()
        
    def browse_vehicles(self, data):
        res = BaseResult()
        res.meta = data.get("meta")
        final_data = data.get("data")
        
        self.display(self.ui.render_vehicle_brief, final_data)
        return res.success()

    def display(self, reder_func, data=None):
        if data:
            self.system_context.set_seen_vehicles(data)
            pagin = self.paginator(data)
            return self.ui.paginator_display(pagin, reder_func, self)

    # def advanced_search(self, criteria):
    #     execution_result = {"ok": True, "payload": None, "error": None, "next": None}
    #     result = self.v_mgr.advanced_search(criteria)

    #     if not result["success"]:
    #         execution_result["ok"] = False
    #         execution_result["error"] = result["error"]
    #         return execution_result
        
    #     display = self.display(self.ui.render_vehicle_brief, result["data"])
    #     execution_result["payload"] = display
    #     return execution_result

    # def vehicles_map(self):
    #     vehicles = self.v_mgr.get_vehicles_data()
    #     ids = list(vehicles.keys())
    #     names = [v_info.get("full_name") for v_info in vehicles.values()]
    #     name_map = self.helpers.mapping_helper(names, ids)
    #     return name_map

    def choose_permission(self):
        permissions = self.permissions.get_role_perms(self.system_context.role)
        index_map = self.helpers.mapping_helper(permissions)
        group = self.ui.role_groups(index_map, self.system_context.role)
        action_map = self.helpers.mapping_helper(permissions[group])
        feature = self.ui.role_features(action_map, group)
        return feature
    
    def check_permission(self, action):
        """
        Checks if the current user can perform an action.
        Returns:
            (bool, str) -> (is_allowed, message)
        """
        result = {"execute": True, "error": None}
        role = self.system_context.role

        if not self.permissions.has_permission(role, action):
            result["execute"] = False 
            result["error"] = f"❌ Your role '{role}' cannot perform '{action}'."

        if action in self.permissions.requires_complete and not self.system_context.is_profile_complete:
            result["execute"] = False 
            result["error"] = "❌ Complete your profile to perform this action."

        return result

    def logout_user(self):
        if not self.system_context.is_authenticated:
            raise SystemExit
        self.system_context.logout()
        return {"status": "logged_out", "role": "guest"}
    
    def run_cycle(self):
        while True:
            feature = self.choose_permission()

            perm_state = self.check_permission(feature)
            if not perm_state["execute"]:
                return {"errors": {"permission": perm_state["error"]}}
            
            self.dispatcher.execute(feature)

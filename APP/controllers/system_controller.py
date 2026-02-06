# APP/controllers/system_controller.py

from APP.core.pipeline.registry import Registry
from APP.core.result.base_result import BaseResult
from APP.core.pipeline.dispatcher import Dispatcher
from APP.core.pipeline.input_pipeline import InputPipeline
from APP.core.initializer.initializer import Initializer


class SystemController:
    """
    Central system controller.
    Holds all system-wide instances, handlers, pipelines, and configuration.
    """

    def __init__(self):
        # ---------------- Build independent components ----------------
        init = Initializer()

        # ---------------- System State ----------------
        self.system_context = init.system_context
        self.permissions = init.permissions

        # ---------------- Helpers & Utilities ----------------
        
        self.collection_helpers = init.collection_helpers
        self.context_helpers = init.context_helpers
        self.system_helpers = init.system_helpers
        self.paginator = init.paginator

        # ---------------- UI ----------------
        self.ui = init.ui

        # ---------------- View Services ----------------
        # Bound services ready to call with render_func and data
        self.view_services = init.view_services

        # ---------------- Domain Models ----------------
        self.user_model = init.user_model

        # ---------------- Domain Managers ----------------
        self.user_manager = init.user_manager
        self.vehicle_manager = init.vehicle_manager

        # ---------------- Domain Handlers ----------------
        self.user_handler = init.user_handler
        self.vehicle_handler = init.vehicle_handler

        # ---------------- Pipeline Configuration ----------------
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

    def auth_flow(self, data):
        res = BaseResult()
        meta, ext_data = self.system_helpers.extract(data)
        res.meta = meta
        self.context_helpers.apply_user_context(self.system_context, ext_data)
        return res.success()

    def vehicles_flow(self, data):
        res = BaseResult()
        meta, ext_data = self.system_helpers.extract(data)
        res.meta = meta
        self.context_helpers.set_seen_vehicles(self.system_context, ext_data)
        self.view_services.render_paginated_view(self.ui, self.paginator, self.ui.render_vehicle_brief, ext_data)
        return res.success()










    def vehicle_details(self, data):
        res = BaseResult()
        meta, ext_data = self.system_helpers.extract(data)
        res.meta = meta
        self.context_helpers.set_seen_vehicles(self.system_context, ext_data)
        self.view_services.render_paginated_view(self.ui, self.paginator, self.ui.render_vehicle_details, ext_data)
        return res.success()


    def choose_permission(self):
        permissions = self.permissions.get_role_perms(self.system_context.role)
        index_map = self.collection_helpers.mapping_helper(permissions)
        group = self.ui.role_groups(index_map, self.system_context.role)
        action_map = self.collection_helpers.mapping_helper(permissions[group])
        feature = self.ui.role_features(action_map, group)
        return feature

    def check_permission(self, action):
        """
        Checks if the current user can perform an action.
        Returns:
            (bool, str) -> (is_allowed, message)
        """
        res = BaseResult()
        role = self.system_context.role

        if not self.permissions.has_permission(role, action):
            return res.fail(f"❌ Your role '{role}' cannot perform '{action}'.")

        if action in self.permissions.requires_complete and not self.system_context.is_profile_complete:
            return res.fail("❌ Complete your profile to perform this action.")
        
        return res.success()
    
    def logout_user(self):
        res = BaseResult()
        if not self.system_context.is_authenticated:
            raise SystemExit
            # return res.fail("Not logged in")

        self.system_context.logout()
        return res.success({"role": "guest"})

    def run_cycle(self):
        res = BaseResult()
        while True:
            feature = self.choose_permission()

            perm_state = self.check_permission(feature)
            if not perm_state.ok:
                return res.fail({"permission": perm_state.error})
            
            self.dispatcher.execute(feature)

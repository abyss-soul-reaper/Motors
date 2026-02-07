from APP.core.pipeline.registry import Registry
from APP.core.result.base_result import BaseResult
from APP.core.pipeline.dispatcher import Dispatcher
from APP.core.pipeline.input_pipeline import InputPipeline
from APP.core.initializer.initializer import Initializer


class SystemController:
    """
    Central orchestrator of the system.

    Responsibilities:
    - Hold system-wide instances
    - Coordinate flows between domain, context, UI, and pipelines
    - Delegate work without implementing business or UI logic
    """

    def __init__(self):
        # ---------------- Build independent components ----------------
        init = Initializer()

        # ---------------- System State ----------------
        self.system_context = init.system_context
        self.permissions = init.permissions

        # ---------------- Helpers ----------------
        self.collection_helpers = init.collection_helpers
        self.context_helpers = init.context_helpers
        self.system_helpers = init.system_helpers

        # ---------------- UI ----------------
        self.ui = init.ui

        # ---------------- View Services ----------------
        self.view_services = init.view_services

        # ---------------- Utilities ----------------
        self.paginator = init.paginator

        # ---------------- Domain ----------------
        self.user_model = init.user_model
        self.user_manager = init.user_manager
        self.vehicle_manager = init.vehicle_manager
        self.user_handler = init.user_handler
        self.vehicle_handler = init.vehicle_handler

        # ---------------- Permissions Flow ----------------
        self.permission_flow = init.permission_flow

        # ---------------- Pipeline Configuration ----------------
        self.feature_config = init.feature_config
        self.system_schema = init.system_schema

        # ---------------- Pipelines ----------------
        self.registry = Registry(self)
        self.input_pipeline = InputPipeline(self.registry, self.system_schema)
        self.dispatcher = Dispatcher(
            self.registry,
            self.system_schema,
            self.input_pipeline,
            self.feature_config,
        )

    # ======================================================
    # Flows
    # ======================================================

    def auth_flow(self, data):
        res = BaseResult()
        meta, ext_data = self.system_helpers.extract(data)
        res.meta = meta

        self.context_helpers.apply_user_context(self.system_context, ext_data)
        return res.success()

    def vehicles_flow(self, data):
        res = BaseResult()
        meta, vehicles = self.system_helpers.extract(data)
        res.meta = meta

        self.view_services.update_seen_vehicles(
            self.context_helpers,
            self.system_context,
            vehicles,
        )

        self.view_services.render_paginated_vehicles(
            self,
            self.ui,
            self.paginator,
            self.ui.render_vehicle_brief,
            vehicles,
        )

        return res.success()

    def vehicle_details(self, data):
        res = BaseResult()
        meta, vehicles = self.system_helpers.extract(data)
        res.meta = meta

        self.view_services.update_seen_vehicles(
            self.context_helpers,
            self.system_context,
            vehicles,
        )

        self.view_services.render_vehicle_details(self.ui, vehicles)
        return res.success()

    # ======================================================
    # Permissions
    # ======================================================

    def choose_permission(self):
        return self.permission_flow.choose_feature(self.system_context.role)

    def check_permission(self, action):
            res = BaseResult()
            role = self.system_context.role

            if not self.permissions.has_permission(role, action):
                return res.fail(f"❌ Your role '{role}' cannot perform '{action}'.")

            if action in self.permissions.requires_complete and not self.system_context.is_profile_complete:
                return res.fail("❌ Complete your profile to perform this action.")

            return res.success()

        # ======================================================
        # Session
        # ======================================================

    def logout_user(self):
        if not self.system_context.is_authenticated:
            raise SystemExit

        self.system_context.logout()
        return BaseResult().success({"role": "guest"})

    # ======================================================
    # Main Loop
    # ======================================================

    def run_cycle(self):
        while True:
            feature = self.choose_permission()

            perm_state = self.check_permission(feature)
            if not perm_state.ok:
                return perm_state

            self.dispatcher.execute(feature)

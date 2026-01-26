from APP.core.helpers import helpers
from APP.ui.user_cli import UserInterface
from APP.models.user_model import UserModel
from APP.core.pipeline.registry import Registry
from APP.core.base.context import SystemContext
from APP.managers.user_manager import UserManager
from APP.schemas.system_schema import SYSTEM_SCHEMA
from APP.core.pagination.pagination import Paginator
from APP.core.pipeline.dispatchers import dispatcher
from APP.managers.vehicles_manager import VehiclesManager
from APP.core.pipeline.feature_config import FEATURE_CONFIG
from APP.core.pipeline.input_pipeline import input_pipeline_dispatcher

class SystemController:
    def __init__(self):
        self.pag = Paginator
        self.helpers = helpers
        self.u_model = UserModel
        self.ui = UserInterface()
        self.u_mgr = UserManager()
        self.config = FEATURE_CONFIG
        self.v_mgr = VehiclesManager()
        self.context = SystemContext()
        self.registry = Registry(self)
        self.sys_schema = SYSTEM_SCHEMA
        self.dispatcher = dispatcher(self)
        self.perms = self.context.permissions_manager

    def register_user(self, data):
        model_result = self.u_model(data).dict_info()
        result = self.u_mgr.register(model_result)
        return self.helpers.update_context(self.context, result)

    def login_user(self, credentials):
        result = self.u_mgr.login(credentials)
        return self.helpers.update_context(self.context, result)
        
    def browse_vehicles(self, vehicles):
        paginator = self.pag(vehicles, per_page=10)
        self.context.set_seen_vehicles(vehicles)
        self.ui.paginator_display(paginator, self.ui.render_vehicle_brief, controller=self)

    def advanced_search(self, criteria):
        results = self.v_mgr.advanced_search(criteria)
        self.context.set_seen_vehicles(results)
        paginator = self.pag(results, per_page=10)
        self.ui.paginator_display(paginator, self.ui.render_vehicle_brief, controller=self)
        return None, True

    def vehicle_details(self):
        v_name = self.ui.vehicle_details_input()
        name_map = self.vehicles_map()

        v_id = name_map.get(v_name)
        if not v_id:
            return None, False
        
        vehicle = self.v_mgr.vehicle_details(v_id)
        if vehicle:
            self.ui.render_vehicle_details(vehicle)
            return None, True
        return None, False

    def vehicles_map(self):
        vehicles = self.v_mgr.get_vehicles_data()
        ids = list(vehicles.keys())
        names = [v_info.get("full_name") for v_info in vehicles.values()]
        name_map = self.helpers.mapping_helper(names, ids)
        return name_map

    def choose_permission(self):
        permissions = self.perms.get_role_perms(self.context.role)
        index_map = self.helpers.mapping_helper(permissions)
        group = self.ui.role_groups(index_map, self.context.role)
        action_map = self.helpers.mapping_helper(permissions[group])
        feature = self.ui.role_features(action_map, group)
        return feature
    
    def check_permission(self, action):
        """
        Checks if the current user can perform an action.
        Returns:
            (bool, str) -> (is_allowed, message)
        """
        role = self.context.role

        if not self.perms.has_permission(role, action):
            return False, f"❌ Your role '{role}' cannot perform '{action}'."

        if action in self.perms.requires_complete and not self.context.is_profile_complete:
            return False, "❌ Complete your profile to perform this action."

        return True, ""

    def logout_user(self):
        if not self.context.is_authenticated:
            raise SystemExit
        self.context.logout()
        return {"status": "logged_out", "role": "guest"}
    
    def run_cycle(self):
        while True:
            feature = self.choose_permission()

            has_perm, perm_msg = self.check_permission(feature)
            if not has_perm:
                return {"errors": {"permission": perm_msg}}
            
            config = self.config.get(feature, {})

            if config["takes_input"]:
                raw_data = self.dispatcher.dispatch_feature_input(feature)
            else: raw_data = None

            if config["use_pipeline"]:
                schema = self.config.get(feature)["schema"]
                errors, pipeline_result = input_pipeline_dispatcher(
                    self, raw_data, schema, self.sys_schema
                )
                if errors:
                    return {"errors": errors}

                data_to_pass = pipeline_result
            else:
                data_to_pass = raw_data

            self.dispatcher.dispatch_feature(feature, data_to_pass)


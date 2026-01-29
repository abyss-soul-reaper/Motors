from APP.core.helpers import helpers
from APP.ui.user_cli import UserInterface
from APP.models.user_model import UserModel
from APP.core.pipeline.registry import Registry
from APP.core.base.context import SystemContext
from APP.managers.user_manager import UserManager
from APP.schemas.system_schema import SYSTEM_SCHEMA
from APP.core.pagination.pagination import Paginator
from APP.core.pipeline.dispatchers import Dispatcher
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
        self.Registry = Registry(self)
        self.config = FEATURE_CONFIG
        self.v_mgr = VehiclesManager()
        self.context = SystemContext()
        self.sys_schema = SYSTEM_SCHEMA
        self.Dispatcher = Dispatcher(self)
        self.pipeline_dsp = input_pipeline_dispatcher
        self.perms = self.context.permissions_manager

    def register_user(self, data):
        execution_result = {"ok": True, "payload": None, "error": None, "next": None}
        model_result = self.u_model(data).dict_info()
        result = self.u_mgr.register(model_result)

        if not result["success"]:
            execution_result["ok"] = False
            execution_result["error"] = result["error"]
            return execution_result

        self.helpers.update_context(self.context, result)
        return execution_result
        
    def login_user(self, credentials):
        execution_result = {"ok": True, "payload": None, "error": None, "next": None}
        result = self.u_mgr.login(credentials)

        if not result["success"]:
            execution_result["ok"] = False
            execution_result["error"] = result["error"]
            return execution_result

        self.helpers.update_context(self.context, result)
        return execution_result
        
    def browse_vehicles(self, vehicles):
        execution_result = {"ok": True, "payload": None, "error": None, "next": None}
        paginator = self.pag(vehicles)
        self.context.set_seen_vehicles(vehicles)
        self.ui.paginator_display(paginator, self.ui.render_vehicle_brief, self)
        return execution_result

    def advanced_search(self, criteria):
        execution_result = {"ok": True, "payload": None, "error": None, "next": None}
        result = self.v_mgr.advanced_search(criteria)

        if not result["success"]:
            execution_result["ok"] = False
            execution_result["error"] = result["error"]
            return execution_result
        
        self.context.set_seen_vehicles(result["data"])
        paginator = self.pag(result["data"])
        self.ui.paginator_display(paginator, self.ui.render_vehicle_brief, self)
        return execution_result

    def vehicle_details(self):
        execution_result = {"ok": True, "payload": None, "error": None, "next": None}
        v_name = self.ui.vehicle_details_input()
        name_map = self.vehicles_map()

        v_id = name_map.get(v_name)
        if not v_id:
            execution_result["ok"] = False
            execution_result["error"] = "Vehicle not found or no results."
            return execution_result
        
        vehicle = self.v_mgr.vehicle_details(v_id)
        if not vehicle["success"]:
            execution_result["ok"] = False
            execution_result["error"] = vehicle["error"]

        self.ui.render_vehicle_details(vehicle)
        return execution_result

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
        result = {"execute": True, "error": None}
        role = self.context.role

        if not self.perms.has_permission(role, action):
            result["execute"] = False 
            result["error"] = f"❌ Your role '{role}' cannot perform '{action}'."

        if action in self.perms.requires_complete and not self.context.is_profile_complete:
            result["execute"] = False 
            result["error"] = "❌ Complete your profile to perform this action."

        return result

    def logout_user(self):
        if not self.context.is_authenticated:
            raise SystemExit
        self.context.logout()
        return {"status": "logged_out", "role": "guest"}
    
    def run_cycle(self):
        while True:
            feature = self.choose_permission()

            perm_state = self.check_permission(feature)
            if not perm_state["execute"]:
                return {"errors": {"permission": perm_state["error"]}}
            
            self.Dispatcher.execute(feature)

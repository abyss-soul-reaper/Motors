from APP.core.utils.pagination import Paginator
from APP.ui.user_cli import UserInterface
from APP.managers.user_manager import UserManager
from APP.managers.vehicles_manager import VehiclesManager
from APP.core.context import SystemContext
from APP.core.utils import helpers
from APP.core.features_registry import Registry
from APP.controllers.features_dispatcher import dispatcher

class SystemController:
    def __init__(self):
        self.ui = UserInterface()
        self.u_mgr = UserManager()
        self.v_mgr = VehiclesManager()
        self.context = SystemContext()
        self.helpers = helpers
        self.registry = Registry(self)
        self.dispatcher = dispatcher(self)
        self.perms = self.context.permissions_manager

    def register_user(self):
        user_data = self.ui.register()
        result = self.u_mgr.register(user_data)
        return self.helpers.update_context(self.context, result)

    def login_user(self):
        credentials = self.ui.login()
        result = self.u_mgr.login(credentials)
        return self.helpers.update_context(self.context, result)
        
    def browse_vehicles(self):
        vehicles = self.v_mgr.browse_vehicles()
        paginator = Paginator(vehicles, per_page=10)
        self.ui.browse_vehicles(paginator)

    def vehicle_details(self):
        vehicles = self.v_mgr.get_vehicles_data()
        ids = list(vehicles.keys())
        names = [v_info.get("model") for v_info in vehicles.values()]
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
        has_perm = self.perms.has_permission(self.context.role, action)
        if has_perm:
            if action in self.perms.requires_complete:
                if not self.context.is_profile_complete:
                    return False
            return True
        return False
        
    def logout_user(self):
        self.context.logout()

    def run_cycle(self):
        while True:
            feature = self.choose_permission()

            if not self.check_permission(feature):
                print("Permission denied or profile incomplete.")

            self.dispatcher.dispatch(feature)
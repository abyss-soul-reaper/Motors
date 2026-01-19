from APP.core.roles import Roles
from APP.core.utils.pagination import Paginator
from APP.ui.user_cli import UserInterface
from APP.managers.user_manager import UserManager
from APP.managers.vehicles_manager import VehiclesManager
from APP.core.context import SystemContext
from APP.core.permissions import Permissions 

class SystemController:
    def __init__(self):
        self.ui = UserInterface()
        self.u_mgr = UserManager()
        self.v_mgr = VehiclesManager()
        self.context = SystemContext()
        self.perms = Permissions()

    def register_user(self):
        user_data = self.ui.register()
        result = self.u_mgr.register(user_data)
        if result["success"]:
            self.context.set_user({
                "user_id": result["user_id"],
                "role": result.get("role", Roles.BUYER),
                "is_profile_complete": result["is_profile_complete"]
            })
            return True
        return False
        
    def login_user(self):
        credentials = self.ui.login()
        result = self.u_mgr.login(credentials)
        if result["success"]:
            self.context.set_user({
                "user_id": result["user_id"],
                "role": result.get("role", Roles.BUYER),
                "is_profile_complete": result.get("is_profile_complete", False)
            })
            return True
        return False
    
    def browse_vehicles(self):
        vehicles = self.v_mgr.browse_vehicles()
        paginator = Paginator(vehicles, per_page=10)
        self.ui.browse_vehicles(paginator)

    def vehicle_details(self):
        vehicles = self.v_mgr.get_vehicles_data()
        ids = list(vehicles.keys())
        names = [v_info.get("model") for v_info in vehicles.values()]
        name_map = self.get_index_map(names, ids)
        return name_map

    def get_index_map(self, keys, values=None):
        object_map = {}
        if values:
            for k, v in zip(keys, values):
                object_map[k] = v
        else:
            for i, obj in enumerate(keys, start=1):
                object_map[i] = obj
        return object_map

    def choose_permission(self):
        permissions = self.perms.get_role_perms(self.context.role)
        index_map = self.get_index_map(permissions)
        group = self.ui.role_groups(index_map, self.context.role)
        action_map = self.get_index_map(permissions[group])
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
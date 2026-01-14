from APP.core.roles import Roles
from APP.ui.user_cli import UserInterface
from APP.managers.user_manager import UserManager
from APP.core.context import SystemContext
from APP.core.permissions import Permissions 

class SystemController:
    def __init__(self):
        self.ui = UserInterface()
        self.u_mgr = UserManager()
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
        else:
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
        else:
            return False

    def get_group_index_map(self):
        permissions = self.perms.get_role_perms(self.context.role)
        index_map = {}
        for i, group_name in enumerate(permissions.keys(), start=1):
            index_map[i] = group_name
        return index_map, permissions
    
    def get_action_index_map(self, actions):    
        action_map = {}
        for i, act in enumerate(actions, start=1):
            action_map[i] = act
        return action_map
    
    def choose_permission(self):
        index_map, permissions = self.get_group_index_map()
        group = self.ui.role_groups(index_map, self.context.role)
        action_map = self.get_action_index_map(permissions[group])
        feature = self.ui.role_features(action_map, self.context.role)
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
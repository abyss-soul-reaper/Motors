from APP.core.roles import Roles
from ui.user_cli import UserInterface
from managers.user_manager import UserManager
from core.context import SystemContext
from core.permissions import Permissions 

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
        
    def show_permissions(self):
        return self.ui.role_features(self.perms, self.context.role)
        
    def check_permission(self, action):
        has_perm = self.perms.has_permission(self.context.role, action)
        if has_perm:
            if action in self.perms._requires_complete:
                if not self.context.is_profile_complete:
                    return False
            return True
        
    def logout_user(self):
        self.context.logout()
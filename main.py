from APP.controllers.system_controller import SystemController
from APP.core.roles import Roles
from APP.ui.user_cli import UserInterface
from APP.managers.user_manager import UserManager
from APP.core.context import SystemContext
from APP.core.permissions import Permissions 
actions = ('Register', 'Login', 'Exit')

class Application:
    def __init__(self):
        self.sys_ctrl = SystemController()
        self.context = SystemContext()

    def run(self):
        while True:
            if self.context.is_authenticated: 
                print(self.sys_ctrl.show_permissions())
                choice = input()
            else:
                print(self.sys_ctrl.show_permissions())
                choice = input()
                # if choice.lower() in ('register', '1'): self.sys_ctrl.register_user()
                # elif  choice.lower() in ('login', '2'): self.sys_ctrl.login_user()
                # elif choice.lower() in ('exit', '3'): break
                # else: pass

if __name__ == "__main__":
    main = Application()
    main.run()
    
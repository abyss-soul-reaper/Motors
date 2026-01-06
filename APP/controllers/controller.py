from controllers.system_controller import SystemController
from APP.core.roles import Roles
from ui.user_cli import UserInterface
from managers.user_manager import UserManager
from core.context import SystemContext
from core.permissions import Permissions 
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
                for i, act in enumerate(actions, start=1): print(f' >{i}. {act}')
                choice = input()
                if choice.lower() in ('register', '1'): self.sys_ctrl.register_user()
                elif  choice.lower() in ('login', '2'): self.sys_ctrl.login_user()
                elif choice.lower() in ('exit', '3'): self.sys_ctrl.logout_user()
                else: pass

if __name__ == "__main__":
    main = Application()
    main.run()
    
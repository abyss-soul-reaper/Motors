from APP.controllers.system_controller import SystemController as sys

class Application:
    def __init__(self):
        self.sys_ctrl = sys()

    def run(self):
        while True:
            if not self.sys_ctrl.context.is_authenticated:
                    # self.sys_ctrl.choose_permission()
                    v = self.sys_ctrl.v_mgr.browsevehicles()
                    for vehicle in v:
                        print(vehicle)
                        break
                    break

if __name__ == "__main__":
    main = Application()
    main.run()

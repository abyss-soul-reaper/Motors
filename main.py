from APP.controllers.system_controller import SystemController as sys

class Application:
    def __init__(self):
        self.sys_ctrl = sys()

    def run(self):
        print("Welcome to the Motors System!")
        self.sys_ctrl.run_cycle()

if __name__ == "__main__":
    main = Application()
    main.run()

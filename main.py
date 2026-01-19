from APP.controllers.system_controller import SystemController as sys

class Application:
    def __init__(self):
        self.sys_ctrl = sys()

    def run(self):
        while True:
            if not self.sys_ctrl.context.is_authenticated:
                    # self.sys_ctrl.choose_permission()
                    # self.sys_ctrl.browse_vehicles()
                    # break
                    # user_input = input("Enter vehicle full name: ").strip()
                    # vehicle_id = self.sys_ctrl.vehicle_details().get(user_input)
                    # if vehicle_id:
                    #     details = self.sys_ctrl.v_mgr.vehicle_details(vehicle_id)
                    #     print (details)
                    # else:
                    #     print("Vehicle not found.")

if __name__ == "__main__":
    main = Application()
    main.run()

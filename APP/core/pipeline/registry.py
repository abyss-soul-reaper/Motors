from APP.core.validation.validators import *

class Registry:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl

    def input_handlers(self):
        return {
            "LOGIN": self.sys_ctrl.ui.login,
            "REGISTER": self.sys_ctrl.ui.register,
            "ADVANCED_SEARCH": self.sys_ctrl.ui.advanced_search_input,
            "VEHICLE_DETAILS": self.sys_ctrl.ui.vehicle_details_input,
        }

    def system_handlers(self):
        return {
            "BROWSE_VEHICLES": self.sys_ctrl.v_handler.browse_vehicles,
            "ADVANCED_SEARCH": self.sysctrl.v_handler.advanced_search,
            "VEHICLE_DETAILS": self.sys_ctrl.v_handler.vehicle_details,
        }

    def execute_handlers(self):
        return {
            "LOGIN": self.sys_ctrl.login_user,
            "REGISTER": self.sys_ctrl.register_user,
            "LOGOUT": self.sys_ctrl.logout_user,
            "BROWSE_VEHICLES": self.sys_ctrl.browse_vehicles,
            "ADVANCED_SEARCH": self.sys_ctrl.advanced_search,
            "VEHICLE_DETAILS": self.sys_ctrl.vehicle_details,
        }

    def validators_handler(self):
        return {
            "type": is_any,
            "year": is_int,
            "ints": is_int,
            "brand": is_any,
            "model": is_any,
            "price": is_float,
            "category": is_any,
            "floats": is_float,
        }

    def normalizers_handler(self):
        return {
            "year": lambda v: v,
            "ints": lambda v: v,
            "price": lambda v: v,
            "floats": lambda v: v,
            "type": lambda v: v.strip(),
            "brand": lambda v: v.strip(),
            "model": lambda v: v.strip(),
            "category": lambda v: v.strip(),
        }

from APP.core.validation.validators import *

class Registry:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl
        self._features_registry = self.register_features()

    def execute_handlers(self):
        EXECUTE_MAP = {
            "LOGIN": self.sys_ctrl.login_user,
            "REGISTER": self.sys_ctrl.register_user,
            "LOGOUT": self.sys_ctrl.logout_user,

            "BROWSE_VEHICLES": self.sys_ctrl.browse_vehicles,
            "ADVANCED_SEARCH": self.sys_ctrl.advanced_search,
            "VEHICLE_DETAILS": self.sys_ctrl.vehicle_details,
        }
        return EXECUTE_MAP
    
    def input_handlers(self):
        INPUT_MAP = {
            "LOGIN": self.sys_ctrl.ui.login,
            "REGISTER": self.sys_ctrl.ui.register,
            
            "ADVANCED_SEARCH": self.sys_ctrl.ui.advanced_search_input,
            "VEHICLE_DETAILS": self.sys_ctrl.ui.vehicle_details_input
        }
        return INPUT_MAP


    def validators_handler(self):
        validators_map = {
            "type": is_any,
            "year": is_int,
            "ints": is_int,
            "brand": is_any,
            "model": is_any,
            "price": is_float,
            "category": is_any,
            "floats": is_float,
            "name": is_non_empty,
            "role": is_valid_role,
            "email": is_valid_email,
            "phone": is_valid_phone,
            "address": is_non_empty,
            "password": is_non_empty
        }
        return validators_map

    def normalizers_handler(self):
        normalizations_map = {
            "year": lambda v: v,
            "ints": lambda v: v,
            "price": lambda v: v,
            "floats": lambda v: v,
            "password": lambda v: v,
            "name": lambda v: v.strip(),
            "type": lambda v: v.strip(),
            "brand": lambda v: v.strip(),
            "model": lambda v: v.strip(),
            "phone": lambda v: v.strip(),
            "address": lambda v: v.strip(),
            "category": lambda v: v.strip(),
            "role": lambda v: v.strip().lower(),
            "email": lambda v: v.strip().lower()
        }
        return normalizations_map

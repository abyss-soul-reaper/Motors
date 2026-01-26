from APP.core.validation.validators import *

class Registry:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl
        self._feature_input_registry = self.register_feature_input()
        self._features_registry = self.register_feature()

    def register_feature_input(self):
        excute_map = {
            "REGISTER": self.sys_ctrl.ui.register,
            "LOGIN": self.sys_ctrl.ui.login,
            "BROWSE_VEHICLES": self.sys_ctrl.v_mgr.browse_vehicles,
            "ADVANCED_SEARCH": self.sys_ctrl.ui.advanced_search_input
        }
        return excute_map
    
    def register_feature(self):
        excute_map = {
            "REGISTER": self.sys_ctrl.register_user,
            "LOGIN": self.sys_ctrl.login_user,
            "LOGOUT": self.sys_ctrl.logout_user,
            "BROWSE_VEHICLES": self.sys_ctrl.browse_vehicles,
            "ADVANCED_SEARCH": self.sys_ctrl.advanced_search
        }
        return excute_map

    def register_validators(self):
        validators_map = {
            "name": is_non_empty,
            "email": is_valid_email,
            "password": is_non_empty,
            "phone": is_valid_phone,
            "address": is_non_empty,
            "role": is_valid_role,
            "brand": is_any,
            "model": is_any,
            "type": is_any,
            "category": is_any,
            "year": is_int,
            "price": is_float,
            "ints": is_int,
            "floats": is_float
        }
        return validators_map

    def register_normalizers(self):
        normalizations_map = {
            "email": lambda v: v.strip().lower(),
            "phone": lambda v: v.strip(),
            "role": lambda v: v.strip().lower(),
            "password": lambda v: v,
            "name": lambda v: v.strip(),
            "address": lambda v: v.strip(),
            "category": lambda v: v.strip(),
            "type": lambda v: v.strip(),
            "brand": lambda v: v.strip(),
            "model": lambda v: v.strip(),
            "year": lambda v: v,
            "price": lambda v: v,
            "ints": lambda v: v,
            "floats": lambda v: v
        }
        return normalizations_map


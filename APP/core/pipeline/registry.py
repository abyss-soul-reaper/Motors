from APP.core.validation.validators import *
from APP.core.base.features_enum import Feature, SpecialFeature

class Registry:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl

    def input_handlers(self):
        INPUT_MAP = {
            Feature.LOGIN: self.sys_ctrl.ui.login,
            Feature.REGISTER: self.sys_ctrl.ui.register,
            
            Feature.ADVANCED_SEARCH: self.sys_ctrl.ui.advanced_search_input,
            SpecialFeature.VEHICLE_DETAILS: self.sys_ctrl.ui.vehicle_details_input
        }
        return INPUT_MAP

    def system_handlers(self):
        SYSTEM_MAP = {
            Feature.REGISTER: self.sys_ctrl.user_handler.register,
            Feature.LOGIN: self.sys_ctrl.user_handler.login,

            Feature.BROWSE_VEHICLES: self.sys_ctrl.vehicle_handler.browse_vehicles,
            Feature.ADVANCED_SEARCH: self.sys_ctrl.vehicle_handler.advanced_search,
            SpecialFeature.VEHICLE_DETAILS: self.sys_ctrl.vehicle_handler.vehicle_details
        }
        return SYSTEM_MAP

    def execute_handlers(self):
        EXECUTE_MAP = {
            Feature.LOGIN: self.sys_ctrl.auth_flow,
            Feature.REGISTER: self.sys_ctrl.auth_flow,
            Feature.LOGOUT: self.sys_ctrl.logout_user,

            Feature.BROWSE_VEHICLES: self.sys_ctrl.vehicles_flow,
            Feature.ADVANCED_SEARCH: self.sys_ctrl.vehicles_flow,
            SpecialFeature.VEHICLE_DETAILS: self.sys_ctrl.vehicle_details
        }
        return EXECUTE_MAP
    
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
            "password": is_non_empty,
            "full_name": is_non_empty
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
            "email": lambda v: v.strip().lower(),
            "full_name": lambda v: v.strip()
        }
        return normalizations_map

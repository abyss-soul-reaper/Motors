class Registry:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl
        self._features_registry = self.register_feature()

    def register_feature(self):
        excute_map = {
            "REGISTER": self.sys_ctrl.register_user,
            "LOGIN": self.sys_ctrl.login_user,
            "LOGOUT": self.sys_ctrl.logout_user,
            "BROWSE_VEHICLES": self.sys_ctrl.browse_vehicles,
            "ADVANCED_SEARCH": ""
        }
        return excute_map
class dispatcher:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl

    def dispatch(self, feature):
        excute_map = self.sys_ctrl.registry._features_registry
        if feature in excute_map:
            return excute_map[feature]()

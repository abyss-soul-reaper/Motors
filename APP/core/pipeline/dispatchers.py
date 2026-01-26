class dispatcher:
    def __init__(self, sys_ctrl):
        self.sys_ctrl = sys_ctrl

    def dispatch_feature_input(self, feature):
        excute_map = self.sys_ctrl.registry._feature_input_registry
        if feature in excute_map:
            return excute_map[feature]()

    def dispatch_feature(self, feature, data=None):
        excute_map = self.sys_ctrl.registry._features_registry
        config = self.sys_ctrl.config.get(feature, {})

        if config.get("takes_input"):
            return excute_map[feature](data)
        else:
            return excute_map[feature]()
        
    def dispatch_validator(self, field, value):
        validators_map = self.sys_ctrl.registry.register_validators()
        if field in validators_map:
            validator =  validators_map[field]
            return validator(value)
        return False
    
    def dispatch_normalizer(self, field, value):
        normalizers_map = self.sys_ctrl.registry.register_normalizers()
        if field in normalizers_map:
            normalizer = normalizers_map[field]
            return normalizer(value)
        return value
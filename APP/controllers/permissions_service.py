class PermissionFlow:
    def __init__(self, permissions, collection_helpers, ui):
        self.permissions = permissions
        self.collection_helpers = collection_helpers
        self.ui = ui

    def choose_feature(self, role):
        perms = self.permissions.get_role_perms(role)

        groups_map = self.collection_helpers.mapping_helper(perms)
        group = self.ui.role_groups(groups_map, role)

        actions_map = self.collection_helpers.mapping_helper(perms[group])
        return self.ui.role_features(actions_map, group)

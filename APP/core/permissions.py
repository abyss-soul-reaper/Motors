from APP.core.base import BaseDataManager
from APP.core.roles import Roles

class Permissions(BaseDataManager):
    """
    Handles role-based permissions for the system.

    This class loads permissions from a JSON file and maps them
    into structured, role-based permission sets. It provides
    utility methods to:
    - Check if a role can perform a specific action
    - Determine whether an action requires a completed user profile

    Permissions are grouped by logical categories (CORE, CART, ORDERS, etc.)
    to keep the system scalable and easy to maintain.
    """

    FILE_PATH = "data/permissions.json"

    def __init__(self):
        """
        Initialize the Permissions manager.

        - Loads the raw permission data from the JSON file.
        - Caches actions that require a completed profile.
        - Maps permissions into role-specific structures
          optimized for fast permission checks.
        """
        super().__init__(self.FILE_PATH)
        self._raw_data = self.load_data()

        self._requires_complete = set(
            self._raw_data.get("REQUIRES_COMPLETE_PROFILE", [])
        )

        self.permissions = self._map_permissions()

    def _map_permissions(self):
        """
        Map raw permission data into role-based permission dictionaries.

        Each role receives:
        - CORE permissions (shared among authenticated roles)
        - Its own feature-specific permission groups

        Returns:
            dict: Mapping of Roles to their permission groups.
        """
        DATA = self._raw_data
        CORE = tuple(DATA.get("CORE_FEATURES", []))

        return {
            Roles.GUEST: DATA.get("GUEST_FEATURES", {}),

            Roles.BUYER: {
                "CORE": CORE,
                **self._to_sets(DATA.get("BUYER_FEATURES", {}))
            },

            Roles.SELLER: {
                "CORE": CORE,
                **self._to_sets(DATA.get("SELLER_FEATURES", {}))
            },

            Roles.ADMIN: {
                "CORE": CORE,
                **self._to_sets(DATA.get("ADMIN_FEATURES", {}))
            }
        }

    def _to_sets(self, features):
        """
        Convert permission lists into sets for faster lookup.

        Args:
            features (dict): Permission groups with action lists.

        Returns:
            dict: Permission groups with actions stored as sets.
        """
        return {
            key: set(values)
            for key, values in features.items()
        }

    def has_permission(self, role, action):
        """
        Check whether a given role is allowed to perform a specific action.

        The method iterates over all permission groups assigned to the role
        (CORE, BROWSING, CART, etc.) and verifies if the action exists in
        any of those groups.

        Args:
            role (Roles): User role (GUEST, BUYER, SELLER, ADMIN).
            action (str): Action identifier to check permission for.

        Returns:
            bool: True if the action is permitted for the role, otherwise False.
        """
        ROLE_PERMISSIONS = self.permissions.get(role, {})
        return any(action in actions for actions in ROLE_PERMISSIONS.values())

    def is_complete_required(self, action):
        """
        Determine whether an action requires a completed user profile.

        Args:
            action (str): Action identifier.

        Returns:
            bool: True if the action requires profile completion, otherwise False.
        """
        return action in self._requires_complete

    def get_role_permissions(self, role):
        return self.permissions.get(role, {})
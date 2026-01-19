from APP.core.roles import Roles
from APP.core.permissions import Permissions

class SystemContext:
    """
    Manages the global state of the currently authenticated user in the system.

    Responsibilities:
    - Keep track of the current user ID and role.
    - Track authentication and profile completion status.
    - Provide a centralized Permissions manager for role-based access control.
    - Reset the system context on logout.

    Attributes:
        user_id (str | None): Unique identifier of the logged-in user. None if guest.
        role (Roles): Current user role (GUEST, BUYER, SELLER, ADMIN).
        is_authenticated (bool): True if a user is logged in, False for guests.
        is_profile_complete (bool): True if the user has completed their profile.
        permissions_manager (Permissions): Instance to check role-based permissions.
    """

    def __init__(self):
        """
        Initialize the system context.

        Sets the default state for a guest user and initializes
        the Permissions manager.
        """
        self.reset()

    def reset(self):
        """
        Reset the context to the default guest state.

        Clears user-specific information and authentication flags,
        useful for logout or system initialization.
        """
        self.user_id = None
        self.role = Roles.GUEST
        self.is_authenticated = False
        self.is_profile_complete = False
        self.permissions_manager = Permissions()

    def set_user(self, user_info):
        """
        Set the current user context after login or registration.

        Args:
            user_info (dict): Dictionary containing user information.
                Expected keys:
                    - "user_id": str, unique identifier of the user.
                    - "role": Roles, the role assigned to the user.
                    - "is_profile_complete": bool, profile completion status.
        """
        self.user_id = user_info.get("user_id")
        self.role = user_info.get("role", Roles.BUYER)
        self.is_authenticated = True
        self.is_profile_complete = user_info.get("is_profile_complete", False)

    def logout(self):
        """
        Log out the current user and reset context to guest state.

        After calling this method:
        - user_id becomes None
        - role becomes Roles.GUEST
        - authentication and profile flags are reset
        - permissions_manager remains initialized
        """
        self.reset()

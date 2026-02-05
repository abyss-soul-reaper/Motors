# =========================
# Context Helpers
# =========================
from APP.core.auth.roles import Roles

def apply_user_context(context, result):
    """
    Update the system context with user info after login/register.
    Only called explicitly in SystemController.
    """
    context.set_user({
        "user_id": result["user_id"],
        "role": result.get("role", Roles.BUYER),
        "is_profile_complete": result.get("is_profile_complete", False)
    })

def set_seen_vehicles(context, vehicles):
    """
    Mark vehicles as seen in the system context.
    """
    context.set_seen_vehicles(vehicles)

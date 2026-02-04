from APP.core.auth.roles import Roles

def update_context(context, result):
        context.set_user({
            "user_id": result["user_id"],
            "role": result.get("role", Roles.BUYER),
            "is_profile_complete": result.get("is_profile_complete", False)
        })

def mapping_helper(keys, values=None):
    object_map = {}
    if values:
        for k, v in zip(keys, values):
            object_map[k] = v
    else:
        for i, obj in enumerate(keys, start=1):
            object_map[i] = obj
    return object_map

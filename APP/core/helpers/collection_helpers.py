# =========================
# Collection / Mapping Helpers
# =========================

def mapping_helper(keys, values=None):
    """
    Creates a mapping from keys to values or to index numbers.
    """
    object_map = {}
    if values:
        for k, v in zip(keys, values):
            object_map[k] = v
    else:
        for i, obj in enumerate(keys, start=1):
            object_map[i] = obj
    return object_map

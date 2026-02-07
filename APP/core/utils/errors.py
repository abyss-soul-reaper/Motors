def wrap_error(stage, feature, error):
    if not isinstance(error, dict):
        error = {"type": "UNKNOWN_ERROR", "reason": error}

    return {
        "code": error.get("type", "UNKNOWN_ERROR"),
        "message": error.get("reason", "Execution failed"),
        "details": {
            "stage": stage,
            "feature": feature,
            "info": error.get("details", None)
        }
    }
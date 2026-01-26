USER_SCHEMA = {
    "name": {
        "type": "string",
        "required": True,
    },
    "email": {
        "type": "email",
        "required": True,
    },
    "password": {
        "type": "password",
        "required": True,
    },
    "role": {
        "type": "role",
        "required": False,
    },
    "phone": {
        "type": "string",
        "required": False,
    },
    "address": {
        "type": "address",
        "required": False,
    }
}

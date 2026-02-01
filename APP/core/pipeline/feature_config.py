from APP.schemas.user_schema import USER_SCHEMA
from APP.schemas.login_schema import LOGIN_SCHEMA
from APP.schemas.search_schema import SEARCH_SCHEMA

FEATURE_CONFIG = {
    "REGISTER": {
        "requires_input": "user",
        "use_pipeline": True,
        "requires_system": False,
        "system_depends_on_input": False,
        "schema": USER_SCHEMA,
    },

    "LOGIN": {
        "requires_input": "user",
        "use_pipeline": True,
        "requires_system": False,
        "system_depends_on_input": False,
        "schema": LOGIN_SCHEMA,
    },

    "ADVANCED_SEARCH": {
        "requires_input": "user",
        "use_pipeline": True,
        "requires_system": True,
        "system_depends_on_input": True,
        "schema": SEARCH_SCHEMA,
    },

    "BROWSE_VEHICLES": {
        "requires_input": None,
        "use_pipeline": False,
        "requires_system": True,
        "system_depends_on_input": False,
        "schema": None,
    },

    "VEHICLE_DETAILS": {
        "requires_input": "mixed",
        "use_pipeline": True,
        "requires_system": True,
        "system_depends_on_input": True,
        "schema": None,
    },

    "LOGOUT": {
        "requires_input": False,
        "use_pipeline": False,
        "requires_system": False,
        "system_depends_on_input": False,
        "schema": None,
    },
}


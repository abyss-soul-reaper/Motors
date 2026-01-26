from APP.schemas.user_schema import USER_SCHEMA
from APP.schemas.login_schema import LOGIN_SCHEMA
from APP.schemas.search_schema import SEARCH_SCHEMA

FEATURE_CONFIG = {
    "REGISTER": {
        "takes_input": True,
        "use_pipeline": True,
        "schema": USER_SCHEMA,
    },

    "LOGIN": {
        "takes_input": True,
        "use_pipeline": True,
        "schema": LOGIN_SCHEMA,
    },

    "ADVANCED_SEARCH": {
        "takes_input": True,
        "use_pipeline": True,
        "schema": SEARCH_SCHEMA,
    },

    "LOGOUT": {
        "takes_input": False,
        "use_pipeline": False,
        "schema": None,
    },

    "BROWSE_VEHICLES": {
        "takes_input": True,
        "use_pipeline": False,
        "schema": None,
    },
}

from APP.schemas.user_schema import USER_SCHEMA
from APP.schemas.login_schema import LOGIN_SCHEMA
from APP.schemas.search_schema import SEARCH_SCHEMA


FEATURE_CONFIG = {

    # ================== AUTH ==================
    "REGISTER": {
        "requires_input": "user",            # UI input
        "use_pipeline": True,
        "schema": USER_SCHEMA,

        "requires_system": False,
        "system_depends_on_input": False,

        "execute_accepts_payload": True,     # register_user(data)
    },

    "LOGIN": {
        "requires_input": "user",
        "use_pipeline": True,
        "schema": LOGIN_SCHEMA,

        "requires_system": False,
        "system_depends_on_input": False,

        "execute_accepts_payload": True,     # login_user(data)
    },

    "LOGOUT": {
        "requires_input": False,
        "use_pipeline": False,
        "schema": None,

        "requires_system": False,
        "system_depends_on_input": False,

        "execute_accepts_payload": False,    # logout_user()
    },


    # ================== VEHICLES ==================
    "BROWSE_VEHICLES": {
        "requires_input": None,              # no UI
        "use_pipeline": False,
        "schema": None,

        "requires_system": True,             # vehicles handler
        "system_depends_on_input": False,

        "execute_accepts_payload": True,     # browse_vehicles(data)
    },

    "ADVANCED_SEARCH": {
        "requires_input": "user",
        "use_pipeline": True,
        "schema": SEARCH_SCHEMA,

        "requires_system": True,
        "system_depends_on_input": True,

        "execute_accepts_payload": True,     # advanced_search(criteria)
    },

    "VEHICLE_DETAILS": {
        "requires_input": "mixed",            # UI + system
        "use_pipeline": True,
        "schema": None,

        "requires_system": True,
        "system_depends_on_input": True,

        "execute_accepts_payload": True,     # vehicle_details(data)
    },
}




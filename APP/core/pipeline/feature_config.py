from APP.domain.user.user_schema import USER_SCHEMA
from APP.domain.vehicle.vehicle_schema import VEHICLE_SCHEMA
from APP.core.base.features_enum import Feature, SpecialFeature

class FeatureResolver:

    @staticmethod
    def resolve(feature):
        """
        feature:
        - str  (from UI / perms.json)
        - Feature enum
        - SpecialFeature enum
        """

        if isinstance(feature, (Feature, SpecialFeature)):
            enum_feature = feature

        elif isinstance(feature, str):
            try:
                enum_feature = Feature[feature]
            except KeyError:
                try:
                    enum_feature = SpecialFeature[feature]
                except KeyError:
                    raise ValueError(f"Unknown feature: {feature}")

        else:
            raise TypeError("Invalid feature type")

        config = FEATURE_CONFIG.get(enum_feature)
        if not config:
            raise ValueError(f"No config found for feature: {enum_feature}")

        return enum_feature, config

FEATURE_CONFIG = {

    Feature.REGISTER: {
        "requires_input": "user",
        "use_pipeline": True,
        "schema": USER_SCHEMA,

        "requires_system": False,
        "system_depends_on_input": False,

        "execute_accepts_payload": True,
    },

    Feature.LOGIN: {
        "requires_input": "user",
        "use_pipeline": True,
        "schema": USER_SCHEMA,

        "requires_system": False,
        "system_depends_on_input": False,

        "execute_accepts_payload": True,
    },

    Feature.LOGOUT: {
        "requires_input": False,
        "use_pipeline": False,
        "schema": None,

        "requires_system": False,
        "system_depends_on_input": False,

        "execute_accepts_payload": False,
    },

    Feature.BROWSE_VEHICLES: {
        "requires_input": None,
        "use_pipeline": False,
        "schema": None,

        "requires_system": True,
        "system_depends_on_input": False,

        "execute_accepts_payload": True,
    },

    Feature.ADVANCED_SEARCH: {
        "requires_input": "user",
        "use_pipeline": True,
        "schema": VEHICLE_SCHEMA,

        "requires_system": True,
        "system_depends_on_input": True,

        "execute_accepts_payload": True,
    },

    SpecialFeature.VEHICLE_DETAILS: {
        "requires_input": "mixed",
        "use_pipeline": True,
        "schema": VEHICLE_SCHEMA,

        "requires_system": True,
        "system_depends_on_input": True,

        "execute_accepts_payload": True,
    },
}

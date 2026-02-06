# APP/core/pipeline/feature_config.py

from APP.domain.user.user_schema import USER_SCHEMA
from APP.domain.vehicle.vehicle_schema import VEHICLE_SCHEMA
from APP.core.base.features_enum import Feature, SpecialFeature

class FeatureResolver:
    """
    Resolves a feature name (str or Enum) into a Feature/SpecialFeature enum
    and its configuration from FEATURE_CONFIG.
    """

    @staticmethod
    def resolve(feature):
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

    # ==================== AUTH FEATURES ====================
    Feature.REGISTER: {
        "requires_input": "user",
        "use_pipeline": True,
        "schema": USER_SCHEMA,

        "requires_system": True,
        "system_depends_on_input": True,

        "execute_accepts_payload": True,
    },

    Feature.LOGIN: {
        "requires_input": "user",
        "use_pipeline": True,
        "schema": USER_SCHEMA,

        "requires_system": True,
        "system_depends_on_input": True,

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

    # ==================== VEHICLE FEATURES ====================
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

    # ==================== SPECIAL FEATURES ====================
    SpecialFeature.VEHICLE_DETAILS: {
        "requires_input": "mixed",
        "use_pipeline": True,
        "schema": VEHICLE_SCHEMA,

        "requires_system": True,
        "system_depends_on_input": True,

        "execute_accepts_payload": True,
    },
}

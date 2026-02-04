# =========================
# Core / Base Context
# =========================
from APP.core.context.system_context import SystemContext
from APP.core.helpers import helpers

# =========================
# UI / Presentation
# =========================
from APP.ui.user_cli import UserInterface

# =========================
# Domain Models & Managers
# =========================
from APP.domain.user.user_model import UserModel
from APP.domain.user.user_manager import UserManager
from APP.domain.vehicle.vehicles_manager import VehiclesManager

# =========================
# Domain Handlers
# =========================
from APP.domain.user.user_handler import UserHandler
from APP.domain.vehicle.vehicle_handler import VehiclesHandler

# =========================
# Pipeline / Execution Infrastructure
# =========================
from APP.core.pipeline.feature_config import FeatureResolver
from APP.schemas.system_schema import SYSTEM_SCHEMA

# =========================
# Utilities
# =========================
from APP.core.pagination.pagination import Paginator


class Initializer:
    """
    Builds all independent system components.
    Does NOT depend on SystemController to avoid circular dependency.
    """

    def __init__(self):
        # ---------------- System State ----------------
        self.system_context = SystemContext()
        self.permissions = self.system_context.permissions_manager

        # ---------------- Helpers & Utilities ----------------
        self.helpers = helpers
        self.paginator = Paginator

        # ---------------- UI ----------------
        self.ui = UserInterface()

        # ---------------- Domain Models ----------------
        self.user_model = UserModel

        # ---------------- Domain Managers ----------------
        self.user_manager = UserManager()
        self.vehicle_manager = VehiclesManager()

        # ---------------- Domain Handlers ----------------
        self.user_handler = UserHandler(self.user_manager)
        self.vehicle_handler = VehiclesHandler(self.vehicle_manager)

        # ---------------- Pipeline Configuration ----------------
        self.feature_config = FeatureResolver()
        self.system_schema = SYSTEM_SCHEMA

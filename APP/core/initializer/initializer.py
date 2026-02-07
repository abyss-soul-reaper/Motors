# APP/core/initializer/initializer.py

# =========================
# Core / Base Context
# =========================
from APP.core.context.system_context import SystemContext
from APP.core.helpers import collection_helpers
from APP.core.context import context_helpers
from APP.core.presentation import view_services
from APP.controllers.system_helpers import SystemHelpers

# =========================
# UI / Presentation
# =========================
from APP.ui.user.user_cli import UserInterface

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
from APP.controllers.permissions_service import PermissionFlow

class Initializer:
    """
    Builds all independent system components.

    Notes:
    - No dependency on SystemController
    - Safe against circular dependencies
    """

    def __init__(self):
        # ---------------- Context & Permissions ----------------
        self.system_context = SystemContext()
        self.permissions = self.system_context.permissions_manager

        # ---------------- UI ----------------
        self.ui = UserInterface()

        # ---------------- Utilities ----------------
        self.paginator = Paginator

        # ---------------- Helpers ----------------
        self.collection_helpers = collection_helpers
        self.context_helpers = context_helpers
        self.system_helpers = SystemHelpers()

        # ---------------- Domain ----------------
        self.user_model = UserModel
        self.user_manager = UserManager()
        self.vehicle_manager = VehiclesManager()

        self.user_handler = UserHandler(self.user_manager, self.user_model)
        self.vehicle_handler = VehiclesHandler(self.vehicle_manager)

        # ---------------- View Services ----------------
        self.view_services = view_services

        # ---------------- Permissions Flow ----------------
        self.permission_flow = PermissionFlow(
            self.permissions,
            self.collection_helpers,
            self.ui,
        )

        # ---------------- Pipeline ----------------
        self.feature_config = FeatureResolver()
        self.system_schema = SYSTEM_SCHEMA

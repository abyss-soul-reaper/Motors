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
    Provides helpers, context, UI, domain models, managers, handlers, and view services.
    """

    def __init__(self):
        # ---------------- System State ----------------
        self.system_context = SystemContext()
        self.permissions = self.system_context.permissions_manager

        # ---------------- UI ----------------
        self.ui = UserInterface()

        # ---------------- Utilities ----------------
        self.paginator = Paginator

        # ---------------- Helpers (low-level) ----------------
        self.collection_helpers = collection_helpers
        self.context_helpers = context_helpers

        # ---------------- Domain Models ----------------
        self.user_model = UserModel

        # ---------------- Domain Managers ----------------
        self.user_manager = UserManager()
        self.vehicle_manager = VehiclesManager()

        # ---------------- System Helpers (depends on managers) ----------------
        self.system_helpers = SystemHelpers()

        # ---------------- Domain Handlers ----------------
        self.user_handler = UserHandler(self.user_manager, self.user_model)
        self.vehicle_handler = VehiclesHandler(self.vehicle_manager)

        # ---------------- View Services ----------------
        # Bound view services ready to use in SystemController
        self.view_services = view_services

        # ---------------- Pipeline Configuration ----------------
        self.feature_config = FeatureResolver()
        self.system_schema = SYSTEM_SCHEMA

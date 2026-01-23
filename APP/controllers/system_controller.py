from APP.core.utils import helpers
from APP.ui.user_cli import UserInterface
from APP.core.context import SystemContext
from APP.core.utils.pagination import Paginator
from APP.core.features_registry import Registry
from APP.managers.user_manager import UserManager
from APP.managers.vehicles_manager import VehiclesManager
from APP.controllers.features_dispatcher import dispatcher

class SystemController:
    def __init__(self):
        self.helpers = helpers
        self.ui = UserInterface()
        self.u_mgr = UserManager()
        self.pag = Paginator
        self.v_mgr = VehiclesManager()
        self.context = SystemContext()
        self.registry = Registry(self)
        self.dispatcher = dispatcher(self)
        self.perms = self.context.permissions_manager

    def register_user(self):
        user_data = self.ui.register()
        result = self.u_mgr.register(user_data)
        return self.helpers.update_context(self.context, result)

    def login_user(self):
        credentials = self.ui.login()
        result = self.u_mgr.login(credentials)
        return self.helpers.update_context(self.context, result)
        
    def browse_vehicles(self):
        vehicles = self.v_mgr.browse_vehicles()
        paginator = self.pag(vehicles, per_page=10)
        self.context.set_seen_vehicles(vehicles)
        self.ui.paginator_display(paginator, self.ui.render_vehicle_brief, controller=self)

    def advanced_search(self):
        criteria = self.ui.advanced_search_input()
        results = self.v_mgr.advanced_search(criteria)
        self.context.set_seen_vehicles(results)
        paginator = self.pag(results, per_page=10)
        self.ui.paginator_display(paginator, self.ui.render_vehicle_brief, controller=self)
        return None, True

    def vehicle_details(self):
        v_name = self.ui.vehicle_details_input()
        name_map = self.vehicles_map()

        v_id = name_map.get(v_name)
        if not v_id:
            return None, False
        
        vehicle = self.v_mgr.vehicle_details(v_id)
        if vehicle:
            self.ui.render_vehicle_details(vehicle)
            return None, True
        return None, False

    def vehicles_map(self):
        vehicles = self.v_mgr.get_vehicles_data()
        ids = list(vehicles.keys())
        names = [v_info.get("full_name") for v_info in vehicles.values()]
        name_map = self.helpers.mapping_helper(names, ids)
        return name_map

    def choose_permission(self):
        permissions = self.perms.get_role_perms(self.context.role)
        index_map = self.helpers.mapping_helper(permissions)
        group = self.ui.role_groups(index_map, self.context.role)
        action_map = self.helpers.mapping_helper(permissions[group])
        feature = self.ui.role_features(action_map, group)
        return feature
        
    def check_permission(self, action):
        has_perm = self.perms.has_permission(self.context.role, action)
        if has_perm:
            if action in self.perms.requires_complete:
                if not self.context.is_profile_complete:
                    return False
            return True
        return False
        
    def logout_user(self):
        if not self.context.is_authenticated:
            raise SystemExit
        self.context.logout()

    def run_cycle(self):
        while True:
            feature = self.choose_permission()

            if not self.check_permission(feature):
                print("Permission denied or profile incomplete.")

            self.dispatcher.dispatch(feature)
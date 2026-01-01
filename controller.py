import cli
import users
import vehicles
import purchases

class HandleActions:
    def __init__(self,ui_obj, usr_mgr_obj, vec_obj):
        self.ui = ui_obj
        self.user = usr_mgr_obj
        self.vehicle = vec_obj

    def start_handling(self, choice, role, user_id):
        if role == 'admin':
            self._handle_admin(choice)
        elif role == 'user':
            self._handle_user(choice, user_id)

    def _handle_admin(self, choice):
        if choice == '1': 
            self.vehicle.view_all_vehicles()
        elif choice == '2': 
            self.vehicle.smart_add_vehicle() 
        elif choice == '3': 
            self.vehicle.update_vehicle_info()
        elif choice == '4': 
            self.vehicle.delete_vehicle()
        elif choice == '5': 
            pass
        elif choice == '6': 
            return "logout"

    def _handle_user(self, choice, user_id):
        if choice == '1': 
            self.vehicle.get_all_available()
        elif choice == '2': 
            self.vehicle.the_finder_interface() 
        elif choice == '3': 
            self.user.add_to_cart(user_id)
        elif choice == '4': 
            self.user.view_my_cart(user_id)
        elif choice == '5': 
            self._process_checkout(user_id)
        elif choice == '6': 
            return "logout"
import cli
import users
import vehicles

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
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass

    def _handle_user(self, choice, user_id):
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
import cli
import users
import vehicles

if __name__ == '__main__':
    ui = cli.UserInterface()
    user_manager = users.UserManager()
    vehicle_manager = vehicles.VehiclesManager()

    while True:
        choice = ui.show_start_menu()

        if choice in ('login', '1'):
            email, password = ui.get_login_input()
            user_id, role, user_name= user_manager.login(email, password)
            if user_id:
                print(f"Welcome You are logged in as a {role}.")
                
            choice = ui.show_internal_menu(role, user_name)    
            if choice == '1':
                pass
            if choice == '2':   
                pass
            if choice == '3':
                pass
            if choice == '4':
                pass
            if choice == '5':
                pass
            if choice == '6':
                pass
        elif choice in ('register', '2'):
            name, email, password, phone, address = ui.get_registration_input()
            
            success = user_manager.register(name, email, password, phone, address)
            if success:
                print("✨ You can now login with your account.")

        elif choice in ('exist', '3'):
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, try again.")
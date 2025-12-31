import cli
import users
import vehicles

if __name__ == '__main__':
    ui = cli.UserInterface()
    user_manager = users.UserManager()
    vehicle_manager = vehicles.VehiclesManager()

    print("\n🚗 Motors Vehicle Ordering System 🏍️")

    while True:
        choice = ui.show_start_menu()

        if choice == 'login':
            email, password = ui.get_login_input()
            user_id, role = user_manager.login(email, password)
            if user_id:
                print(f"Welcome You are logged in as a {role}.")
                break
        if choice == 'register':
            name, email, password, phone, address = ui.get_registration_input()
            
            success = user_manager.register(name, email, password, phone, address)
            if success:
                print("✨ You can now login with your account.")
        if choice == 'exist':
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.")
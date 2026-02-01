from datetime import datetime
from APP.core.validation.validators import *
class UserInterface:
    def __init__(self):
        pass

    def register(self):
        print("\n--- Register New Account ---")

        name = input('Name: ')
        while not name:
            name = input('❌ Name is required: ')

        email = input('Email: ')
        while not (email and is_valid_email(email)):
            email = input("❌ Invalid Email. Try again: ")

        password = input('Password: ')
        while not password:
            password = input('❌ Password is required: ')

        confirm_password = input("Confirm Password: ")
        while confirm_password != password:
            print("❌ Passwords do not match!")
            confirm_password = input("Try again: ")

        role = input("Enter role (buyer/seller)(default buyer): ")
        if not (role and is_valid_role(role)):
            print("❌ Invalid role. Defaulting to 'buyer'.")
            role = "buyer"

        user_data = {
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }
        
        print("\nOptional: Complete your profile? (y/n)")
        if input('>> ') == 'y':
            
            phone = input('Phone: ')
            while not (phone and is_valid_phone(phone)):
                phone = input('❌ Invalid Egyptian Phone: ')

            address = input('Address: ')
            while not address:
                address = input('❌ Address can\'t be empty: ')

            user_data["phone"] = phone
            user_data["address"] = address
            user_data["is_profile_complete"] = True

        user_data["created_at"] = datetime.now().isoformat()

        return user_data

    def login(self):
        print("\n--- User Login ---")

        email = input('Email: ')
        while not (email and is_valid_email(email)):
            email = input("❌ Invalid Email. Try again: ")

        password = input('Password: ')
        while not password:
            password = input('❌ Password is required: ')

        return {"email": email, "password": password}

    @staticmethod
    def role_groups(index_map, role):
        """
        Print all permission groups.
        """
        print(f"\n=== {role} Features ===")
        for i, group in index_map.items():
            print(f"-- {i}. {group} --")

        group_choice = input("Select a group number to view actions: ")
        while not group_choice.isdigit() or int(group_choice) not in index_map:
            group_choice = input("❌ Invalid choice. Select a valid group number: ")

        return index_map[int(group_choice)]

    @staticmethod
    def role_features(action_map, group):
        print(f"\n=== {group} Actions ===")
        for i, act in action_map.items():
            print(f"-- {i}. {act} --")

        action_choice = input("Select action number :")
        while not action_choice.isdigit() or int(action_choice) not in action_map:
            action_choice = input("❌ Invalid choice. Select a valid action number: ")
        return action_map[int(action_choice)]

    def paginator_display(self, paginator, render_fn, sys_ctrl=None):
        print("\n--- Available Vehicles ---")
        page_num = 1
        commands = {
        'n': lambda: paginator.next(current_page),
        'p': lambda: paginator.prev(current_page),
        's': lambda: sys_ctrl.dispatcher.execute("ADVANCED_SEARCH") if sys_ctrl else None,
        'd': lambda: sys_ctrl.vehicle_details() if sys_ctrl else None,
        'q': lambda: paginator.quit(),
        }
        try:
            while True:
                count = 1
                page = paginator.get_page(page_num)
                items = page.get("items", [])
                current_page = page.get("current_page", 1)
                total_pages = page.get("total_pages", 1)

                if not items:
                    print("No available vehicles at the moment.")
                    return
                
                print(f"--- Page {current_page} of {total_pages} ---\n")

                for vehicle in items:
                    render_fn(vehicle, count)
                    count += 1

                print("\nn - Next Page | p - Previous Page | s - Search | d - Details | q - Quit Browsing")
                cmd = input("\nEnter command: ")
                action = commands.get(cmd)

                if action:
                    if cmd in {'s', 'd'} and sys_ctrl:
                        result = action()
                        if not result["ok"]:
                            print(f"\n{result["error"]}")
                    else:
                        result = action()
                        if not result["can_move"] and cmd in {'n', 'p'}:
                            print(f"\n{result["error"]}")
                else:
                    print("\nInvalid command. Please try again.")

        except StopIteration:
            print("\nExiting vehicle browsing.")

    @staticmethod
    def render_vehicle_brief(vehicle, count):
        print(f'\n{str(count).zfill(2)}. Full Name: {vehicle.get("full_name"):<40} | Price: {vehicle.get("price"):<10,}$')
        
    @staticmethod
    def render_vehicle_details(vehicle, count=None):

        print("\n--- Vehicle Details ---")
        print("-" * 50)
        print(f"Full Name: {vehicle.get('full_name'):<30}")
        print(f"Brand    : {vehicle.get('brand'):<10}")
        print(f"Model    : {vehicle.get('model'):<30}")
        print(f"Type     : {vehicle.get('type'):<5}")
        print(f"Category : {vehicle.get('category'):<15}")
        print(f"Price    : {vehicle.get('price'):<10,} $")
        print(f"Year     : {vehicle.get('year'):<5}")
        print("-" * 50 + "\n")

    def advanced_search_input(self):
        print("\n--- Advanced Vehicle Search ---")

        PRICE_OPTIONS = {
            1: ("Under or equal to 50,000", 50_000),
            2: ("Under or equal to 100,000", 100_000),
            3: ("Under or equal to 500,000", 500_000),
            4: ("Under or equal to 1,000,000", 1_000_000),
            5: ("Under or equal to 3,000,000", 3_000_000),
            6: ("Any", None)
        }

        brand = input("Brand (leave blank to skip): ")
        model = input("Model (leave blank to skip): ")
        category = input("Category (leave blank to skip): ")
        
        year_input = input("Year (leave blank to skip): ")
        year = int(year_input) if year_input.isdigit() else None

        print("\nPrice Options:")
        for i,(label, _) in PRICE_OPTIONS.items():
            print(f"{i}. {label}")

        price_input = input("Max Price (leave blank to skip): ")
        price = PRICE_OPTIONS.get(int(price_input), (None, None))[1] if price_input else None

        criteria = {
            "brand": brand if brand else None,
            "model": model if model else None,
            "category": category if category else None,
            "year": year,
            "price": price
        }

        return criteria
    
    def vehicle_details_input(self):
        v_name = input("Enter Vehicle Full Name for details: ")
        while not v_name:
            v_name = input("❌ Vehicle name cannot be empty. Try again: ")
        return {"full_name": v_name}
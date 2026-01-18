import re
from datetime import datetime
from APP.models.user_model import UserModel
from APP.core.utils.validators import is_valid_email, is_valid_phone, is_valid_role
class UserInterface:
    def __init__(self):
        pass

    def register(self):
        print("\n--- Register New Account ---")

        name = input('Name: ').strip().title()
        while not name:
            name = input('❌ Name is required: ').strip().title()

        email = input('Email: ').strip().lower()
        while not (email and is_valid_email(email)):
            email = input("❌ Invalid Email. Try again: ").strip().lower()

        password = input('Password: ').strip()
        while not password:
            password = input('❌ Password is required: ').strip()

        confirm_password = input("Confirm Password: ").strip()
        while confirm_password != password:
            print("❌ Passwords do not match!")
            confirm_password = input("Try again: ").strip()

        role = input("Enter role (buyer/seller)(default buyer): ").strip().lower()
        if not (role and is_valid_role(role)):
            print("❌ Invalid role. Defaulting to 'buyer'.")
            role = "buyer"

        user_data = UserModel(None, name, email, password, role=role)

        print("\nOptional: Complete your profile? (y/n)")
        if input('>> ').strip().lower() == 'y':
            
            phone = input('Phone: ').strip()
            while not (phone and is_valid_phone(phone)):
                phone = input('❌ Invalid Egyptian Phone: ').strip()

            address = input('Address: ').strip().title()
            while not address:
                address = input('❌ Address can\'t be empty: ').strip().title()
            
            user_data.phone = phone
            user_data.address = address
            user_data.is_profile_complete = True

        user_data.created_at = datetime.now().isoformat()

        return user_data.dict_info()

    def login(self):
        print("\n--- User Login ---")

        email = input('Email: ').strip().lower()
        while not (email and is_valid_email(email)):
            email = input("❌ Invalid Email. Try again: ").strip().lower()

        password = input('Password: ').strip()
        while not password:
            password = input('❌ Password is required: ').strip()

        return {"email": email, "password": password}
    
    @staticmethod
    def role_groups(index_map, role):
        """
        Print all permission groups.
        """
        print(f"\n=== {role} Features ===")
        for i, group in index_map.items():
            print(f"-- {i}. {group} --")

        group_choice = input("Select a group number to view actions: ").strip()
        while not group_choice.isdigit() or int(group_choice) not in index_map:
            group_choice = input("❌ Invalid choice. Select a valid group number: ").strip()

        return index_map[int(group_choice)]

    @staticmethod
    def role_features(action_map, group):
        print(f"\n=== {group} Actions ===")
        for i, act in action_map.items():
            print(f"-- {i}. {act} --")

        action_choice = input("Select action number :")
        while not action_choice.isdigit() or int(action_choice) not in action_map:
            action_choice = input("❌ Invalid choice. Select a valid action number: ").strip()
        print(action_map[int(action_choice)])
        return action_map[int(action_choice)]

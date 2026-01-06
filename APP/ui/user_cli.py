import re
from datetime import datetime
from models.user_model import UserModel
from core.utils.validators import is_valid_email, is_valid_phone
from core.permissions import Permissions
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
        if not role:
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
    def role_features(permissions, role):
        """
        Print all permission groups and actions for a given role.
        """
        role_perms = permissions.get_role_permissions(role)
        print(f"\n=== {role} Features ===")
        for group, actions in role_perms.items():
            print(f"{group}: {', '.join(actions)}")

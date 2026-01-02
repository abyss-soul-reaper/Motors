import uuid
import hashlib
import re
from datetime import datetime
from base import BaseDataManager

class UserManager(BaseDataManager):
    HASH_ALGORITHM = "sha256"
    PHONE_PATTERN = r'^01[0125]\d{8}$'
    EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def __init__(self):
        super().__init__(r'users.json')
    @staticmethod
    def _hash_password(password):
        hash_obj = hashlib.new(UserManager.HASH_ALGORITHM)
        hash_obj.update(password.encode())
        return hash_obj.hexdigest()
    
    def register(self, user_data, user_role='user'):
        if not re.match(self.EMAIL_PATTERN, user_data["email"]):
            print("❌ Error: Invalid email format.")
            return False
        if user_data.get("phone"):
            if not re.match(self.PHONE_PATTERN, user_data["phone"]):
                print("❌ Error: Invalid Egyptian phone number.")
                return False
        
        users= self.load_data()

        for usr_data in users.values():
            if usr_data['email'] == user_data["email"]:
                print("❌ Error: Email already registered.")
                return False
        
        user_id = str(uuid.uuid4())
        hashed_pwd = self._hash_password(user_data["password"])
        user_role = user_role.lower()

        users[user_id] = {
            "name": user_data['name'],
            "email": user_data['email'],
            "password": hashed_pwd,
            "user_role": user_role,
            "created_at": datetime.now().isoformat()
        }
        if user_data.get("phone"): users[user_id]["phone"] = user_data["phone"]
        if user_data.get("address"): users[user_id]["address"] = user_data["address"]

        self.save_data(users)
        print(f"✅ Success: New {user_role} account created for '{user_data["name"]}'.")
        return True
    
    def authenticate(self, user_data):
        users = self.load_data()
        hashed_input = self._hash_password(user_data['password'])

        for user_id, usr_data in users.items():
            if usr_data['email'] == user_data["email"] and usr_data['password'] == hashed_input:
                print(f"🔓 Login successful! Welcome, {usr_data['name']}.")
                return user_id, usr_data
        
        print("⚠️ Login Failed: Check your email or password.")
        return None, None
    
    def add_to_cart(self, user_id):
        pass

    def view_my_cart(self, user_id):
        pass

    def clear_cart(self, user_id):
        pass
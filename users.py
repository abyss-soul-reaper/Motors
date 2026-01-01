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

    def _hash_password(self, password):
        hash_obj = hashlib.new(self.HASH_ALGORITHM)
        hash_obj.update(password.encode())
        return hash_obj.hexdigest()
    
    def register(self, name, email, password, phone, address, user_role='user'):
        if not re.match(self.EMAIL_PATTERN, email):
            print("❌ Error: Invalid email format.")
            return False
        if not re.match(self.PHONE_PATTERN, phone):
            print("❌ Error: Invalid Egyptian phone number.")
            return False
        
        users= self.load_data()

        for user_data in users.values():
            if user_data['email'] == email:
                print("❌ Error: Email already registered.")
                return False
        
        user_id = str(uuid.uuid4())
        hashed_pwd = self._hash_password(password)
        user_role = user_role.lower()

        users[user_id] = {
            "name": name,
            "email": email,
            "password": hashed_pwd,
            "phone": phone,
            "address": address,
            "user_role": user_role,
            "created_at": datetime.now().isoformat()
        }

        self.save_data(users)
        print(f"✅ Success: New {user_role} account created for '{name}'.")
        return True
    
    def login(self, email, password):
        users = self.load_data()
        hashed_input = self._hash_password(password)

        for user_id, user_data in users.items():
            if user_data['email'] == email and user_data['password'] == hashed_input:
                print(f"🔓 Login successful! Welcome, {user_data['name']}.")
                return user_id, user_data['user_role'], user_data['name']
        
        print("⚠️ Login Failed: Check your email or password.")
        return None, None
    
    def add_to_cart(self, user_id):
        pass

    def view_my_cart(self, user_id):
        pass

    def clear_cart(self, user_id):
        pass
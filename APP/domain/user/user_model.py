from datetime import datetime
from APP.core.validation.validators import *
from APP.core.security.security import hash_password

class UserModel:
    def __init__(self, data):
        self.user_id = data.get("user_id")
        self.name = data.get("name")
        self.email = data.get("email")
        self.password = data.get("password")
        self.phone = data.get("phone")
        self.role = data.get("role", "buyer")
        self.address = data.get("address")
        self.is_profile_complete = data.get("is_profile_complete", False)
        self.created_at = data.get("created_at", datetime.now().isoformat())

        self.normalize_fields()
        self.validate()

    def normalize_fields(self):
        self.name = self.name.strip().title()
        self.role = self.role.strip().lower()
        self.email = self.email.strip().lower()
        if self.phone: self.phone = self.phone.strip()
        if self.address: self.address = self.address.strip().title()

    def validate(self):
        if not is_non_empty(self.name):
            raise ValueError("Name cannot be empty")
        if self.phone and not is_valid_phone(self.phone):
            raise ValueError("Invalid phone number")
        if not is_valid_role(self.role):
            raise ValueError(f"Invalid role: {self.role}")
        if not is_valid_email(self.email):
            raise ValueError("Invalid email")
        if not is_non_empty(self.password):
            raise ValueError("Password cannot be empty")

    def dict_info(self):
        return {
            "basic_info": {
                "name": self.name,
                "email": self.email,
                "password": self.password
            },
            "contact_info": {
                "phone": self.phone,
                "address": self.address
            },
            "account": {
                "role": self.role,
                "is_profile_complete": self.is_profile_complete,
                "created_at": self.created_at
            }
        }

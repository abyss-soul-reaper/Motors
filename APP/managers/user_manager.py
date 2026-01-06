import uuid
from core.base import BaseDataManager
from core.utils.security import hash_password
from core.utils.validators import is_valid_email, is_valid_phone

class UserManager(BaseDataManager):
    FILE_PATH = r'data\users.json'

    def __init__(self):
        super().__init__(self.FILE_PATH)

    def register(self, user_data):
        email = user_data.get("basic_info", {}).get("email", "").lower()
        phone = user_data.get("contact_info", {}).get("phone", "")

        if not is_valid_email(email):
            return {
                "success": False,
                "error": "Invalid email address"
            }

        if phone and not is_valid_phone(phone):
            return {
                "success": False,
                "error": "Invalid phone number"
            }

        users = self.load_data()

        for usr_data in users.values():
            if usr_data["basic_info"]["email"].lower() == email:
                return {
                "success": False,
                "error": "Email already exists"
            }

        user_data.pop("user_id", None)  # Ensure user_id is not set
        user_data["user_id"] = str(uuid.uuid4())
        hashed_pwd = hash_password(user_data["basic_info"]["password"])
        user_data["basic_info"]["password"] = hashed_pwd
        users[user_data["user_id"]] = user_data

        self.save_data(users)
        return {
        "success": True,
        "user_id": usr_data["user_id"],
        "role": usr_data["account"]["role"],
        "is_profile_complete": usr_data["account"]["is_profile_complete"]
    }

    def login(self, user_data):
        users = self.load_data()

        email = user_data.get("email", "").lower()
        password = user_data.get("password", "")
        hashed_pwd = hash_password(password)

        for usr_data in users.values():
            if (
                usr_data["basic_info"]["email"].lower() == email.lower()
                and usr_data["basic_info"]["password"] == hashed_pwd
                ):
                return {
                "success": True,
                "user_id": usr_data["user_id"],
                "role": usr_data["account"]["role"],
                "is_profile_complete": usr_data["account"]["is_profile_complete"]
            }

        return {
        "success": False,
        "error": "Invalid email or password"
    }
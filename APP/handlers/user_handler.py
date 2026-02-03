import uuid
from APP.core.security.security import hash_password
from APP.core.validation.validators import is_valid_email, is_valid_phone

class UserHandler:
    def __init__(self, u_mgr):
        self.u_mgr = u_mgr

    def register(self, user_data):
        result = {"success": False, "data": None, "error": None, "meta": None}

        email = user_data.get("basic_info", {}).get("email", "").lower()
        phone = user_data.get("contact_info", {}).get("phone", "")

        if not is_valid_email(email):
            result["error"] = "Invalid email address"
            return result

        if phone and not is_valid_phone(phone):
            result["error"] = "Invalid phone number"
            return result

        users = self.u_mgr.get_all_users()

        for usr_data in users.values():
            if usr_data["basic_info"]["email"].lower() == email:
                result["error"] = "Email already exists"
                return result

        user_data.pop("user_id", None)
        user_id = str(uuid.uuid4())
        user_data["basic_info"]["password"] = hash_password(
            user_data["basic_info"]["password"]
        )
        self.u_mgr.save_user(user_id, user_data)

        result["success"] = True
        result["data"] = {
            "user_id": user_id,
            "role": user_data["account"]["role"],
            "is_profile_complete": user_data["account"]["is_profile_complete"]
        }

        return result

    def login(self, user_data):
        result = {"success": False, "data": None, "error": None, "meta": None}

        users = self.u_mgr.get_all_users()
        email = user_data.get("email", "").lower()
        password = hash_password(user_data.get("password", ""))

        for u_id, u_data in users.items():
            if (
                u_data["basic_info"]["email"].lower() == email
                and u_data["basic_info"]["password"] == password
            ):
                result["success"] = True
                result["data"] = {
                    "user_id": u_id,
                    "role": u_data["account"]["role"],
                    "is_profile_complete": u_data["account"]["is_profile_complete"]
                }
                return result
            
        result["error"] = "Invalid email or password"
        return result

import uuid
from APP.domain.user.auth_result import AuthResult
from APP.core.security.security import hash_password
from APP.core.validation.validators import is_valid_email, is_valid_phone

class UserHandler:
    def __init__(self, u_mgr):
        self.u_mgr = u_mgr

    def register(self, user_data):
        res = AuthResult()

        email = user_data.get("basic_info", {}).get("email", "").lower()
        phone = user_data.get("contact_info", {}).get("phone", "")

        if not is_valid_email(email):
            return res.fail("Invalid email address")

        if phone and not is_valid_phone(phone):
            return res.fail("Invalid phone number")

        users = self.u_mgr.get_all_users()

        for usr_data in users.values():
            if usr_data["basic_info"]["email"].lower() == email:
                return res.fail("Email already exists")

        user_data.pop("user_id", None)
        user_id = str(uuid.uuid4())
        user_data["basic_info"]["password"] = hash_password(
            user_data["basic_info"]["password"]
        )
        self.u_mgr.save_user(user_id, user_data)

        res.payload["user_id"] = user_id
        res.payload["role"] = user_data["account"]["role"]
        res.payload["is_profile_complete"] = user_data["account"]["is_profile_complete"]

        return res.success()

    def login(self, user_data):
        res = AuthResult()

        users = self.u_mgr.get_all_users()
        email = user_data.get("email", "").lower()
        password = hash_password(user_data.get("password", ""))

        for user_id, user_data in users.items():
            if (
                user_data["basic_info"]["email"].lower() == email
                and user_data["basic_info"]["password"] == password
            ):
                res.payload["user_id"] = user_id
                res.payload["role"] = user_data["account"]["role"]
                res.payload["is_profile_complete"] = user_data["account"]["is_profile_complete"]

                return res.success()
            
        return res.fail("Invalid email or password")

class UserModel:
    def __init__(self, data):
        self.user_id = data.get("user_id", None)
        self.name = data.get("name")
        self.email = data.get("email")
        self.password = data.get("password")
        self.phone = data.get("phone", None)
        self.address = data.get("address", None)
        self.role = data.get("role", "buyer")
        self.is_profile_complete = data.get("is_profile_complete", False)
        self.created_at = data.get("created_at")

        self.normalize_fields()

    def normalize_fields(self):
        if self.name:
            self.name = self.name.title()
        if self.address:
            self.address = self.address.title()
        if self.email:
            self.email = self.email.lower()

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

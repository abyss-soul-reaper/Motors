class UserModel:
    def __init__(self, user_id, name, email, password, phone=None, address=None,
                 role="buyer", is_profile_complete=False, created_at=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.role = role
        self.is_profile_complete = is_profile_complete
        self.created_at = created_at

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

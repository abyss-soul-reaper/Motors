from APP.core.result.base_result import BaseResult

class AuthResult(BaseResult):
    def __init__(self):
        super().__init__()
        self.payload = {
            "user_id": None,
            "role": None,
            "is_profile_complete": None
        }
from APP.core.base.base import BaseDataManager

class UserManager(BaseDataManager):
    FILE_PATH = r'data\users.json'

    def __init__(self):
        super().__init__(self.FILE_PATH)

    def get_all_users(self):
        return self.load_data()

    def get_user_by_id(self, user_id):
        users = self.get_all_users()
        return users.get(user_id)

    def save_user(self, user_id, user_data):
        users = self.get_all_users()
        users[user_id] = user_data
        self.save_data(users)

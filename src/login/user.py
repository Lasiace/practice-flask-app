from flask_login import UserMixin

class User(UserMixin):
    @staticmethod
    def find_user(user_id):
        return User('dummy')

    def __init__(self, username):
        self.username = username

    def get_name(self):
        return self.username

    def get_id(self):
        return chr(1)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    def get_name(self):
        return self.username

    def get_id(self):
        return self.user_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
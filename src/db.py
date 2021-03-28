import sqlite3
import uuid
import bcrypt
import random
import string

def create_fake_hashed_password():
    return bytes("$2b$12$" + ''.join(random.SystemRandom().choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 53)), "utf-8")

class Database():
    def __init__(self, database_loc):
        self.database_loc = database_loc

    def with_db_connection(func):
        def wrapper(self, *args, **kwargs):
            database = sqlite3.connect(self.database_loc)
            retval = func(self, database, *args, **kwargs)
            database.close()
            return retval
        return wrapper

    @with_db_connection
    def find_user_info(self, database, user_id = None, username = None):
        if not user_id and not username:
            raise Exception("Must pass either user_id and username to {0:s}".format(find_user_info.__name__))
        if user_id and username:
            raise Exception("Cannot pass both user_id and username to {0:s}".format(find_user_info.__name__))

        cursor = database.cursor()
        if user_id:
            cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        elif username:
            cursor.execute("SELECT * FROM users WHERE name=?", (username,))
        values = cursor.fetchone()

        if values:
            column_names = map(lambda x: x[0], cursor.description)
            return dict(zip(column_names, values))
        return None

    # checkpw and create_fake_hashed_password is always called in both branches to prevent timing attacks
    @with_db_connection
    def check_user_pw(self, database, username, password):
        user_info = self.find_user_info(username = username)
        unicode_password = bytes(password, "utf-8")
        fake_hashed_password = create_fake_hashed_password()
        if user_info:
            return bcrypt.checkpw(unicode_password, bytes(user_info['password'], "utf-8"))
        bcrypt.checkpw(unicode_password, fake_hashed_password)
        return False

db = Database("test.db")
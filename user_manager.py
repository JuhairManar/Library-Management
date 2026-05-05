from users import User

class UserManager:
    def __init__(self):
        self.users = {}

    def register(self, name, roll, password):
        if roll in self.users:
            print("Account already exists")
            return None

        user = User(name, roll, password)
        self.users[roll] = user
        return user

    def login(self, roll, password):
        user = self.users.get(roll)
        if user and user.password == password:
            return user
        return None

    def get_user(self, roll):
        return self.users.get(roll)
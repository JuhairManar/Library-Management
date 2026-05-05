from .users import User

class UserManager:
    def __init__(self):
        self.users={}

    def register(self,name,roll,password):
        if roll in self.users:
            print("Account already exists")
            return None

        user=User(name,roll,password)
        self.users[roll]=user
        return user

    def login(self,roll,password):
        if roll in self.users and self.users[roll].password==password:
            return self.users[roll]
        return None

    def get_user(self,roll):
        return self.users.get(roll)
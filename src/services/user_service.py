from src.models.User import User


class UserService:
    def __init__(self):
        self.users={}
        
    def add_user(self,id,name,email):
        user=User(id,name,email)
        self.users[id]=user
        return user
    def get_user(self,id):
        return self.users.get(id)    
    
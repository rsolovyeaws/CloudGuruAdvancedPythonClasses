# Take away: Use self.__class__. to access class variable

class User:
    active_users = []
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __comparable(self):
        return {key : value.lower() for key, value in self.__dict__.items()}
    
    def __eq__(self, other):
        return self.__comparable() == other.__comparable()
    
    def __ne__(self, other):
        return self.__comparable() != other.__comparable()
    
    def activate(self):
        if not self.is_active():
            self.__class__.active_users.append(self)
            
    def deactivate(self):
        if self.is_active():
            self.__class__.active_users.remove(self)
    
    def is_active(self):
        return self in self.__class__.active_users
    
me = User("Robert", "rs@gmail.com")

me.activate()
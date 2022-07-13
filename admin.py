# AdminPrivs.py has the objects that calls class from admin.py
# This file process works when running AdminPrivs.py


# Create two classes
# One class named User (Parent)
# One Class name Admin(child-inherits)
# Print the Name and Privileges associated to those names

class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, privileges):
        super().__init__(name)
        self.privileges = privileges

def show_privileges(self):
    print(self.name, self.privileges)








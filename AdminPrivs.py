# Run AdminPrivs.py file as this file, because admin has the classes we are calling from
# Import the admin.py file
# Create class Admin_privs
# Create a data set that assigns the 9 privileges
# Assign the data sets as privileges to the Ceo, Senior, and Junior managers
# Assign the names of the Ceo as Mr. Smith, Senior as Mr. Anderson, and Junior as Mr. Wayne
# Display the privileges for each manager

import admin

class Admin_privs:
    def __init__(self, name, privileges):
        self.name = name
        self.privileges = privileges

privilege_1 = str("Can add posts")
privilege_2 = str("Can delete posts")
privilege_3 = str("Can edit posts")
privilege_4 = str("Can add others to posts")
privilege_5 = str("Can remove others from posts")
privilege_6 = str("Can add people to platform")
privilege_7 = str("Can remove people from platform")
privilege_8 = str("Can ban people from platform")
privilege_9 = str("Can delete platform")

ceo_privileges = [privilege_1, privilege_2, privilege_3, privilege_4, privilege_5, privilege_6, privilege_7,
                privilege_8, privilege_9]
senior_manager_privileges = [privilege_1, privilege_2, privilege_3, privilege_4, privilege_5, privilege_6,
                            privilege_7]
junior_manager_privileges = [privilege_1, privilege_2, privilege_3]

ceo = admin.Admin("Mr. Smith", ceo_privileges)
ceo.privileges = ceo_privileges
admin.show_privileges(ceo)

senior = admin.Admin("Mr. Anderson", senior_manager_privileges)
senior.privileges = senior_manager_privileges
admin.show_privileges(senior)

junior = admin.Admin("Mr. Wayne", junior_manager_privileges)
junior.privileges = junior_manager_privileges
admin.show_privileges(junior)

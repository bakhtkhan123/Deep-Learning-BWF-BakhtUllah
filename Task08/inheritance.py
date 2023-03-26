# Exercise 9.6 IceCreamStand
from class_restaurant import Restaurant,User
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor=[]
    def display_flavor(self):
        '''we have the following IceCream flavor available'''
        for flavor in self.flavor:
            print(flavor)
IceCreamStand_0=IceCreamStand('chips','indian')
IceCreamStand_0.flavor=["vanilla", "chocolate", "strawberry"]
IceCreamStand_0.describe_restaurant()
IceCreamStand_0.display_flavor()

# Exercise 9.7 Admin

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilages=['can_add_post','can_delete_post','can_ban_post']
    def show_privilages(self):
        for post in self.privilages:
            print(post)
    
admin=Admin('bakht','maseed')
admin.privilages=['add_post_1','del_post_2','ban_post_3']
admin.show_privilages()

# Exercise 9.8 privilages
class Privilage:
    def __init__(self):
        self.privilages=['add_post','del_post','ban_post']
    def show_privilages(self):
        for post in self.privilages:
            print(post)
    
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilages=Privilage()
            
admin_1=Admin('sami','Aziz')
admin_1.privilages.show_privilages()   




    
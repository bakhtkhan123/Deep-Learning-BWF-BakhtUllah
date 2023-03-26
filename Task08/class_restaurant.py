# Exercise 9.1
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("my restaurant name is "+ self.restaurant_name.title()+'.')
        print('Its type is '+self.cuisine_type.title()+'.')
    def open_restaurant(self):
        print("the restaurant is open")
restaurant=Restaurant('slice of spice','french cuisine')
print('my restaurant name is '+ restaurant.restaurant_name.title()+'.')
print('my cuisine type is '+ restaurant.cuisine_type.title()+'.')
print('==================================')
# restaurant.restaurant_name
# restaurant.cuisine_type
restaurant.describe_restaurant()
restaurant.open_restaurant()

print('============================')
# Exercise 9.2
restaurant_1=Restaurant('chops and hops','greek cuisine')
restaurant_2=Restaurant('food truck','spanish cuisine')
restaurant_3=Restaurant('food hall','german cuisine')
restaurant_1.describe_restaurant()
print('=============================')
restaurant_2.describe_restaurant()
print('=============================')
restaurant_3.describe_restaurant()

# Exercise 9.3
class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        print('my first name is '+self.first_name.title()+'.')
        print('my last name is '+self.last_name.title()+'.')
    def greet_user(self):
        print('Hi how are you! '+self.first_name.title()+' '+self.last_name.title()+'.')
user_1=User('bakht','maseed')
user_2=User('danish','khan')
print('================================')
user_1.greet_user()
print('================================')
user_1.describe_user()
print('============================')
user_2.describe_user()

# Exercise 9.4 number served
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.served_number=0
    def describe_restaurant(self):
        print("my restaurant name is "+ self.restaurant_name.title()+'.')
        print('Its type is '+self.cuisine_type.title()+'.')
    def open_restaurant(self):
        print("the restaurant is open")
    def set_number_served(self,number):
         self.served_number=number
    def increment_number_served(self,increment):
        self.served_number+=increment

restaurant_0=Restaurant('panda Express','chinees')
print(restaurant_0.restaurant_name+' has served '+ str(restaurant_0.served_number)+' customer.')
restaurant_0.set_number_served(50)
print(restaurant_0.restaurant_name+' has served '+ str(restaurant_0.served_number)+' customer.')
restaurant_0.increment_number_served(5)
print(restaurant_0.restaurant_name+' has served '+ str(restaurant_0.served_number)+' customer.')
        


# Exercise 9.5 login attempt
class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attampts=0
    def describe_user(self):
        print('my first name is '+self.first_name.title()+'.')
        print('my last name is '+self.last_name.title()+'.')
    def greet_user(self):
        print('Hi how are you! '+self.first_name.title()+' '+self.last_name.title()+'.')
        
    def increment_login_attampt(self):
        self.login_attampts+=1

    def reset_login_attampt(self):
        self.login_attampts=0
        
user_0=User('inayat','ullah')
user_0.increment_login_attampt()
user_0.increment_login_attampt()
user_0.increment_login_attampt()
user_0.increment_login_attampt()
print(user_0.first_name+' made '+ str(user_0.login_attampts)+' login attampts.')
user_0.reset_login_attampt()
print(user_0.first_name+' made '+ str(user_0.login_attampts)+' login attampts.')




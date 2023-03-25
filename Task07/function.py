# Excercise 8.1
def display_message():
    print("Hi everyone in this chapter we will learn about function in python")
display_message()

# Excercise 8.2
def favorite_book(Title):
    print("One of my favorite book is "+ Title.title()+" in the computer science")
favorite_book('python crush')

# Excercise 8.3
def make_shirt(size,text):
    ''' Display text on the shirt and this is my docstring'''
    print('\nMy shirt size is '+ str(size) +' and my name is '+ text.title()+".")
make_shirt(56,'Babar Azam')#positional argument passing
make_shirt(text='Rizwan',size=78)#keyword arugument passing

# Excercise 8.4
def Make_shirt(size='large',text='I Love Python'):
    if size=='large':
        print('\nthe size of my shirt is '+size.title()+' and '+text.title()+".")
    elif size=='medium':
        print('\nthe size of my shirt is '+size.title()+' and '+text.title()+'.')
    else:
        print('\nthe size of my shirt is '+size.title()+ ' and '+text.title()+'.')
Make_shirt('large')
Make_shirt('medium')
Make_shirt('small','I have different size of shirt')

# Exercise 8.5
def describe_city(city,country='pakistan'):
    print(city.title()+' is in '+country.title())
describe_city('lahore')
describe_city('karachi')
describe_city('kabul','afghanistan')


    
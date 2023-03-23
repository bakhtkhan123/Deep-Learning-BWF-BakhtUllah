# creating a dictionary Ex 6.1
person={'First_name':'Bakht','Last_name':'Ullah','Age':23,'City':'Mianwali'}
print(person['First_name'])
print(person['Last_name'])
print(person['Age'])
print(person['City'])

#adding element to the dictionary
person['Gender']='Male'
print(person)

#removing element from the dict
del person["Gender"]
print(person)

# Ex 6.2
Favorate_numbers = {
    'sami':25,
    'raza':15,
    'asad':55,
    'razaq':99,
    'samad':1
    }
print("sami's favorate_numbers is "+ 
    str(Favorate_numbers['sami']).title()+
    '.')
#Favorate_numbers['sami']


    
    


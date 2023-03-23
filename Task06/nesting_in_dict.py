# Ex 6.7
people_1={'bakht':'python','inayat':'c++','bilal':'java'}
people_2={'anas':'html','jawad':'css','danish':'bootstrap'}
people_3={'kashif':'node js','umair':'flutter','junaid':'marn stack'}

peoples=[people_1,people_2,people_3]
for people in peoples:
    print(people) 
    
# Ex 6.9
favorite_places={
    'bilal':['murree','naran','kaghan'],
    'bakht':['waziristan','para chinaar','kurma'],
    'moazam':['kashmir','sakardu','anarkali']
    }
friend_1=input('Enter your name=')
f1_fav_place=input('enter your favorite palces =')
friend_2=input('enter you name=')
f2_fav_place=input('enter you favorite places=')

f1_place_list=f1_fav_place.split(',')
f2_place_list=f2_fav_place.split(',')

favorite_places[friend_1]=f1_place_list
favorite_places[friend_2]=f2_place_list

for key , value in favorite_places.items():
    print('\n key: '+ key)
    val=','.join(value)
    print('value: ' + val)
print(favorite_places)

# Ex 6.11
users={'Bilal':
    {'first':'bilal','last':'khan','city':'mianwali'},
    'Bakht':
    {'first':'bakht','last':'maseed','city':'D I khan'},
    'Moazam':
    {'first':'Moazam','last':'sardar','city':'kashmir'}
    }
for name,user_info in users.items():
    print('\nName ='+name.title())
    full_name=user_info['first'] + " " + user_info['last']
    location=user_info['city']
    print("\tfull_name: " + full_name.title())
    print("\tcity: "+ location.title())
    
    

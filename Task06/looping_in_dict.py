# Ex 6.3&4
Glossary={
    'list':'it is mutable',
    'tupel':'it is immutable',
    'set':'it contain unique values',
    'if_else': 'conditional stmt',
    'git':'used for version control'
    }
    
Glossary['str concate']='we combine multiple string with + sign'
Glossary['for_loop']='this kind of loop we use for finite value'
Glossary['while-loop']='this kind of loop we use for infinite value'
Glossary['prompt input']='to take input from the user'

for key, value in Glossary.items():
    print("\nkey: "+ key)
    print("values: "+ value)
    
# Ex 6.5
River={'Nile':'Eygpt','Indus':'Pakistan','Amazon':'America'}
for key,value in River.items():
    print('The '+ key.title()+' runs through '+ value.title()+'.')
    
for key in sorted(River.keys()):
    print('key '+ key.title())
    
for value in River.values():
    print('value '+ value.title())
    
# Ex 6.6
favorite_language={'Inayat':'Python','Bakht':'C++','Bilal':'JS'}
person_to_poll=['Anas','Bakht','Sharjeel','Danish','Inayat']
for people in person_to_poll:
    if people in favorite_language:
        print("thank you "+ people.title() + " for your polling")
    else: 
        print('please '+ people.title() + ' take your favorite programming language and let us know')
    
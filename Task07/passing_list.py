# Exercise 8.9
def show_magician(names):
    for i in names:
        print('magician '+ i.title()+' is here!')
names=['salman','nawaz','shedi']
show_magician(names)

print('============================')

# Exercise 8.10
def make_great(magician):
    for i in range(len(magician)):
        magician[i]='the great '+ magician[i]
magician=['asad','hamza','ali']
make_great(magician)
print(magician) # checking magician list
show_magician(magician)# Exercise 8.9 function show_magician called

print('=============================')

# Exerxise 8.11 (modified Exercise 8.10)
def make_great(magician):
    great=[]
    for i in magician:
        great_name='the great '+ i.title()
        great.append(great_name)
    return great
def show_magician(name):
    for i in name:
        print(i.title())
names=['bakht','bilal','zubair']
great_names=make_great(names[:])
show_magician(names)
show_magician(great_names)
        


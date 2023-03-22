# enumerate function in loop // this function gives us the key vaue pair
tupples=("bird","hen","duck")
for tupple in enumerate(tupples):
    print(tupple)

y=enumerate(tupples)
print(list(y))


print(y)

# we can also set the index by ourself
for i in enumerate(tupples,10):
    print(i)
    

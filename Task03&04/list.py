# Name: Bakht Ullah

# string concatenation
message="Hello world!"
course="I am learning crush course on python"
concate=message +course
print(concate)
print("My name is"+" Bakht ullah")


#striping Whitespace
favorate_Language= ' Python '
print(favorate_Language.rstrip())
print(favorate_Language.lstrip())


''' Creating List
list can be string type integer type '''
List=["apple","mango","banana","orange","grapes"]
# Access first element from the list
print(List[0])

# Modify element of the list
List[2]="pomegranate"
print(List)

# Adding element to the list
List.append("appricot")
print(List)

# Inserting element to the list
List.insert(0,"one")
print(List)

# Removing element using pop from the list
List.pop(1)
print(List)

# Removing element using value
List.remove('appricot')
print(List)

# Organizing a list
List.sort()
print(List)

# Reversing list
List.reverse()
print(List)

# Finding Length of list
print(len(List))

#Looping on list
for i in List:
    print(i)
    

#tupple we cannot add or removing element to tuple as it is immutable
tupples=(10,20,30)
print(tupples)
tupples=(100,200,300)
print(tupples)
for tupple in tupples:
    print(tupple)



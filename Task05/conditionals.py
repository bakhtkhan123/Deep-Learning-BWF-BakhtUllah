#simple if else stmt
num=input("Enter code key '123' to execute the remaining code = ")
if num=="123":
    print("code executed successfully")
else:
    print("you entered the worng code key")
    
#simple if elif else stmt
code=input("Enter code key 'S' to start the code =  ")
if code=='S':
    print("code run successfully with large S")
elif code=='s':
    print("code run successfully with small s")
else:
    print("you entered the wrong code key")
    
#nested if
num=int(input('Enter a number = '))
if num >= 10:
    print('first if executed')
    num1=num
    if num1 > 10:
        print('second if is also executed')
    
    
    
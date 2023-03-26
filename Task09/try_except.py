#print(5/0)

try:
    print(5/0)
except:
    print('zero division error')
    
    
print('give me two number I will divide them')
print('enter q to quit the program')

while True:
    num1=input('enter first number')
    if num1=='q':
        break
    num2=input('enter second number')
    if num2=='q':
        break
    try:
        answer=int(num1)/int(num2)
        print(answer)
    except:
        print('zero division error')
    
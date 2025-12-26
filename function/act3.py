'''
Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform.
 Take user input whatever operation they want to perform And call that function accordingly.
'''

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
op=input("Choose the operation that you need to perform.1. + 2. - 3. * 4. /")
n1=int(input('Enter the first number:'))
n2=int(input('Enter the second number:'))
if op=='+':
    print('The sum is ',add(n1,n2))
elif op=='-':
    print('The sub is ',sub(n1,n2))
if op=='+':
    print('The sum is ',add(n1,n2))
if op=='+':
    print('The sum is ',add(n1,n2))

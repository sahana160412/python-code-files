'''Write a program to return the addition of numbers of two different lists.
 Then, display a list that is square of numbers of another list.
 Use the map() function here to get the desired result.'''

number1=[1,3,5]
number2=[2,4,6]
result=map(lambda x,y:x+y,number1,number2)
print('The addition of two numbers is',list(result))

nl=[1,6,7,8]
print('the new list is',nl)
def square(n):
    return n*n
multiply=map(square,nl)
print(list(multiply))
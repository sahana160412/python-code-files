'''Write a program to perform the following operations: 1. Create a tuple with different datatypes 
2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4.
 Count the occurrences of an element in the tuple 5. Perform slicing on the tuple'''
 
tuple_1=(3,9.4,True,'HELLO')
print(tuple_1)
tuple_2=(23,44,76,90,54)
print(tuple_2)
tuple_3=tuple_2+(9,)
print(tuple_3)
tuple_4=(34,56,34,69,69,56,73,43)
print(tuple_4.count(56))
tuple_5=('j','a','c','k')
print(tuple_5[0:3])



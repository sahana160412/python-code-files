'''Write a program to create a set and perform the following operations on that set- 
1. Create a set with integer elements 
2. Create a set with mixed data type elements 
3. Create another set with elements - 1, 2, 3, 4, 3, 2 
4. Create a set from a list with elements - [1, 2, 3, 2]
5. Print the set after removing the first element from this set - [0, 1, 3, 4, 5]'''

s1={1,3,2,3,4,5,6,6,6}
print(s1)
s2={-23,5.78,5.78,-879,34,-23}
print(s2)
s3={-1,2,3,4,3,2}
print(s3)
s4=set([1,2,3,2])
print(s4)
print('the data type of s4 is',type(s4))
s5=[0,1,3,4,5]
print(s5)
print('the data type of s5 is',type(s5))
s5.pop(0)
print('the list after removing the first item is',s5)
s6=set(s5)
print('the set is',s6)
print('the data type of s6 is',type(s6))
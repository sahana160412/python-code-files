"""Write a program to reverse the string entered by the user."""
n=input("enter the string:")
rev=""
for u in n:
    rev=u+rev
print(rev)
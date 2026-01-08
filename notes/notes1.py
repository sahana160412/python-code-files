#try, except , finally example
a = 14
b = 13
try:
    print(a)
    print(b)
    print(c)
except :
    print('NameError: variable is not defined')
finally :
    print(a+b)

#raise keyword example

age = 21
try:
    if age < 18:
        raise ValueError
    else:
        print('You are eligible to vote!')

except ValueError as e:
    print('You are not eligible as you are under 18')
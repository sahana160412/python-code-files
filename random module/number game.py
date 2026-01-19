import random
games=True
number=str(random.randint(12,23))
print("I will generate a number from 10 to 22, and you have to guess the number one digit at the time.")
print("the game ends when u get 1 hero!")

while games:
    guess=input("Enter your best guess:")
    if number == guess:
        print("the number is correct")
        print("the number is",number)
        break
    else:
        print("find the another chance")
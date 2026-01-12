def check_age():
    while True:
        try:
            age_input = input("Please enter your age: ")
            age = int(age_input)
            if age <= 0:
                print("Error: Age must be a positive number. Please try again.")
                continue
            break

        except ValueError:

            print("Error: Invalid input. Please enter a numerical value for your age.")

    if age % 2 == 0:
        print(f"You entered {age}. Your age is an even number.")
    else:
        print(f"You entered {age}. Your age is an odd number.")
check_age()
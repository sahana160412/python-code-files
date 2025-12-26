#declaration of a function
def sample():
    print('Hello World!')
#calling a function
sample()

#Arguments
def studentDetails(name, age):
    print('The Name is ', name)
    print('The Age is ', age)
studentDetails('sahana', 13)

#function return
def display(name, school):
    return name, school
print(display('Krish','DPS'))
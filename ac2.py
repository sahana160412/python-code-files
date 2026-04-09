class Employee:
    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Destructor called object deleted")
def create_obj():
        print("Making Object...")
        obj= Employee()
        print("Function end...")
        return obj
print("Calling Create_obj() function....")
obj = create_obj()
print("programe End")
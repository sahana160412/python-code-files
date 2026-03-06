class Dog:
    species = "Canine"
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
    def display_details(self):
        print(f"Species: {Dog.species}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years\n")
dog1 = Dog("Golden Retriever", 5)
dog2 = Dog("German Shepherd", 3)
print("--- Dog 1 Details ---")
dog1.display_details()

print("--- Dog 2 Details ---")
dog2.display_details()

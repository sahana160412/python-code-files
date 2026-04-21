class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        return amount + (0.1 * amount) # Adds 10% extra fee
my_bus = Bus(50)
print(my_bus.fare())

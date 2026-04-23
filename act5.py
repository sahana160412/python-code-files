class BMW:
    def fuel_type(self):
        return "petrol"
    def max_speed(self):
        return "250 km/h"
class Ferrari:
    def fuel_type(self):
        return "petrol"
    def max_speed(self):
        return "340km/h"
for car in (BMW(), Ferrari()):
    print(car.fuel_type())
    print(car.max_speed())
    print()
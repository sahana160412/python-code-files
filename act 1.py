class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed= max_speed
        self.mileage= mileage
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is{capacity} passengers"
    def __str__(self):
        return f"Name:{self.name} speed:{self.max_speed} mileage:{self.mileage}"
class bus(vehicle):
    pass
school_bus=bus("school volvo",180,12)
print(school_bus)
school_bus.seating_capacity(12)

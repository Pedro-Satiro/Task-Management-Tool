class Vehicle:

    def __init__(self, name, speed):

        self.name = name

        self.speed = speed

 

    def get_speed(self):

        return f"{self.name} runs at {self.speed} km/h"

class Car(Vehicle):

    def __init__(self, name, speed, brand):

        super().__init__(name, speed)

        self.brand = brand

 

car = Car("Fusion", 200, "Ford")

print(car.get_speed())

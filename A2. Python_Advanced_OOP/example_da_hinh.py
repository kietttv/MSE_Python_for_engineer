class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def move(self):
        print("Drive!")

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

# Create a Car class
car1 = Car("Ford", "Mustang")

# Create a Boat class
boat1 = Boat("Ibiza", "Touring 20")

# Create a Plane class
plane1 = Plane("Boeing", "747")

# polymorphism
for x in (car1, boat1, plane1):
    x.move()
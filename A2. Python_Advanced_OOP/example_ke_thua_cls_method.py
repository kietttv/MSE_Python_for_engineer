class Vehicle:
    brand_name = 'BMW'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_price(cls, name, price):
        # Convert price to dollars (example conversion)
        ind_price = price * 75
        # Create new Vehicle object
        return cls(name, ind_price)

    def show(self):
        print(self.name, self.price)


class Car(Vehicle):
    def average(self, distance, fuel_used):
        mileage = distance / fuel_used
        print(self.name, 'Mileage', mileage)


# Create an object of Car
bmw_us = Car('BMW X5', 65000)
bmw_us.show()

# Class method of parent class is available to child class
# This will return the object of the calling class
bmw_ind = Car.from_price('BMW X5', 65000)
bmw_ind.show()

# Check type
print(type(bmw_ind))

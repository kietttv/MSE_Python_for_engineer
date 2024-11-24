class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("Hello my name is: " + self.name)         

p1 = Person("Kiet", 21)
p1.greenting()   
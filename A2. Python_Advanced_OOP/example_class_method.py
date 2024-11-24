class Student:
    school_name = "Greenwich"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, school_name):
        cls.school_name = school_name

    def show(seft):
        print(seft.name, seft.age, seft.school_name)

kiet = Student("Kiet", 21)
kiet.show()

Student.change_school("FPT")
kiet.show()
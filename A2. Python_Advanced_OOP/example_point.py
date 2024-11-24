class Point:
    numberOfPoint = 0

    def __init__(self, x, y):
        self.x = x
        self.y =y
        Point.numberOfPoint += 1;

    def get_x(self):
        return self.x

    def get_y(seft):
        return seft.y

    def print_point(seft):
        print('Class attribue, Poin #', Point.numberOfPoint)
        print("Instance  attribue, Poin #", seft.numberOfPoint)
        print('(%d, %d)' % (seft.get_x(), seft.get_y()))    

p1 = Point(2, 3)
p1.print_point()

p2 = Point(-2, -3)
p2.print_point()

p3 = Point(3, 3)
p3.print_point()

print("",Point.numberOfPoint, p1.get_x(), p1.get_y())
print("",Point.numberOfPoint, p2.get_x(), p2.get_y())
print("",Point.numberOfPoint, p3.get_x(), p3.get_y())
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()



r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)


print("Area of Rectangle 1:", r1.area())
print("Area of Rectangle 2:", r2.area())


if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 has smaller or equal area")


class Rectangle:

    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.__length

    @staticmethod
    def checking_data(value):
        if not (isinstance(value, (int, float))):
            raise TypeError("U must enter a number(int or float)")
        if not 0 < value < 20:
            raise ValueError("Length should be > 0 and < 20")

    @length.setter
    def length(self, value):
        self.checking_data(value)
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.checking_data(value)
        self.__width = value

    def perimeter_count(self):
        return round(2 * (self.__width + self.__length), 2)

    def area_count(self):
        return round(self.__length * self.__width, 2)

    def __str__(self):
        return f'My rectangle perimeter: {self.perimeter_count()}\nMy rectangle area: {self.area_count()}'


my_rectangle = Rectangle(14.5, 13.3)
print(my_rectangle)
try:
    my_rectangle.length = float(input('Enter length: '))
    my_rectangle.width = float(input('Enter width: '))
except ValueError or TypeError or EOFError:
    print('Incorrect input u should write a number')
    exit()
print(my_rectangle)

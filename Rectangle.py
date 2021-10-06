class Rectangle:
    length = 1
    width = 1

    def set_length_and_width(self, length, width):
        if not isinstance(length, float) or not isinstance(width, float):
            raise TypeError("U must enter a number")
        if (0 < length < 20) and (0 < width < 20):
            self.length = length
            self.width = width
        else:
            raise TypeError('Length and width should be > 0 and < 20')

    def get_length_and_width(self):
        return self.length, self.width

    def perimeter_count(self):
        perimeter = 2 * sum(self.get_length_and_width())
        return round(perimeter, 2)

    def area_count(self):
        area = self.length * self.width
        return round(area, 2)


my_rectangle = Rectangle()
user_rectangle = Rectangle()
my_rectangle.set_length_and_width(14.5, 13.3)
print("My rectangle perimeter: " + str(my_rectangle.perimeter_count()) +
      "\nMy rectangle area: " + str(my_rectangle.area_count()))

try:
    length_inp = float(input('Enter length: '))
    width_inp = float(input('Enter width: '))
except ValueError or TypeError or EOFError:
    print('Incorrect input u should write a number')
    exit()
user_rectangle.set_length_and_width(length_inp, width_inp)
print(
    "My rectangle perimeter: " + str(user_rectangle.perimeter_count()) +
    "\nMy rectangle area: " + str(user_rectangle.area_count())
)

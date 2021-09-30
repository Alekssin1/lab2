class Rectangle:
    length = 1
    width = 1

    def set_length_and_width(self, length, width):
            if (0<length<20) and (0<width<20) and length and width:
                self.length = length
                self.width  = width
                ind = 1
            else:
                print('Length and width should be > 0 and < 20')
                exit()


    def get_length_and_width(self):
        return self.length, self.width


    def perimeter_count(self):
        perimeter = 2 * sum(self.get_length_and_width())
        return perimeter

    def area_count(self):
        area = self.length * self.width
        return area


my_rectangle = Rectangle()
try:
    my_rectangle.set_length_and_width( 14.5, 13)
    print(my_rectangle.perimeter_count())
    print(my_rectangle.area_count())
except ValueError or KeyboardInterrupt or NameError:
    print('You must enter an digit')

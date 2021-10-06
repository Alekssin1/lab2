from math import gcd


class Rational:

    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int) or denominator == 0:
            raise TypeError("Incorrect input! Variable type must be int! Denominator can't be zero!")
        self.__numerator = numerator
        self.__denominator = denominator
        self.new_numerator = 1
        self.new_denominator = 1

    def reduction(self):
        """ find greatest common divider of two integers and reduce fraction"""
        divider = gcd(self.__numerator, self.__denominator)
        return self.__numerator // divider, self.__denominator // divider

    @staticmethod
    def checking_second_number(second_numerator, second_denominator):
        """ check whether the fraction is entered correctly """
        if not isinstance(second_numerator, int) or not isinstance(second_denominator, int) or second_denominator == 0:
            raise TypeError("Incorrect input! Variable type must be int! Denominator can't be zero!")
        else:
            return True

    def add(self, new_numerator, new_denominator):
        if self.checking_second_number(new_numerator, new_denominator):
            self.__numerator = self.__numerator * new_denominator + new_numerator * self.__denominator
            self.__denominator = self.__denominator * new_denominator

    def sub(self, new_numerator, new_denominator):
        if self.checking_second_number(new_numerator, new_denominator):
            self.__numerator = self.__numerator * new_denominator - new_numerator * self.__denominator
            self.__denominator = self.__denominator * new_denominator

    def multi(self, new_numerator, new_denominator):
        if self.checking_second_number(new_numerator, new_denominator):
            self.__numerator = self.__numerator * new_numerator
            self.__denominator = self.__denominator * new_denominator

    def div(self, new_numerator, new_denominator):
        if self.checking_second_number(new_numerator, new_denominator) and new_numerator != 0:
            self.__numerator = self.__numerator * new_denominator
            self.__denominator = self.__denominator * new_numerator
        elif new_numerator == 0:
            raise ZeroDivisionError("Division by zero, try again!")

    def get_fraction(self):
        """ return fraction in form numerator/denominator """
        return f"{int(self.reduction()[0])}/{int(self.reduction()[1])}"

    def get_floating(self):
        """ return fraction in floating-point format """
        return round(self.reduction()[0] / self.reduction()[1], 2)


rational = Rational(3, 6)
print(rational.get_fraction(), rational.get_floating())
rational.add(1, 5)
print("1/2 + 1/5 = ", rational.get_fraction(), '=', rational.get_floating())
rational.sub(1, 10)
print("7/10 - 1/10 = ", rational.get_fraction(), '=', rational.get_floating())
rational.multi(4, 5)
print("3/5 * 4/5 = ", rational.get_fraction(), '=', rational.get_floating())
rational.div(1, 5.2)
print("12/25 / 1/5.2 = ", rational.get_fraction(), '=', rational.get_floating())

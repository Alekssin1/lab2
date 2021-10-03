import math


class Rational:

    def __init__(self, numerator=1, denominator=1):
        if type(numerator) != int or type(numerator) != int or denominator == 0:
            raise TypeError("Incorrect input! Variable type must be int! Denominator can't be zero!")
        self.__numerator = numerator
        self.__denominator = denominator

    def reduction(self):
        if type(self.__numerator / self.__denominator) != 0:
            return self.__numerator / math.gcd(self.__numerator, self.__denominator), self.__denominator / math.gcd(
                self.__numerator, self.__denominator)
        else:
            return self.__numerator, self.__denominator

    def add(self, new_numerator, new_denominator):
        if type(new_numerator) != int or type(new_numerator) != int or new_denominator == 0:
            raise TypeError("Incorrect input! Variable type must be int! Denominator can't be zero!")
        self.__numerator = self.__numerator * new_denominator + new_numerator * self.__denominator
        self.__denominator = self.__denominator * new_denominator

    def sub(self, new_numerator, new_denominator):
        if type(new_numerator) != int or type(new_numerator) != int or new_denominator == 0:
            raise TypeError("Incorrect input! Variable type must be int! Denominator can't be zero!")
        self.__numerator = self.__numerator * new_denominator - new_numerator * self.__denominator
        self.__denominator = self.__denominator * new_denominator

    def multi(self, new_numerator, new_denominator):
        if type(new_numerator) != int or type(new_numerator) != int or new_denominator == 0:
            raise TypeError("Incorrect input! Variable type must be int! Denominator can't be zero!")
        self.__numerator = self.__numerator * new_numerator
        self.__denominator = self.__denominator * new_denominator

    def div(self, new_numerator, new_denominator):
        if type(new_numerator) != int or type(new_numerator) != int or new_denominator == 0:
            raise TypeError("Incorrect input! Variable type must be int! Denominator can't be zero!")
        self.__numerator = self.__numerator * new_denominator
        self.__denominator = self.__denominator * new_numerator

    def get_fraction(self):
        return f"{int(self.reduction()[0])}/{int(self.reduction()[1])}"

    def get_floating(self):
        return self.reduction()[0] / self.reduction()[1]


rational = Rational(3, 6)
print(rational.get_fraction(), rational.get_floating())
rational.add(1, 5)
print("1/2 + 1/5 = ", rational.get_fraction(), '=', rational.get_floating())
rational.sub(1, 10)
print("7/10 - 1/10 = ", rational.get_fraction(), '=', rational.get_floating())
rational.multi(4, 5)
print("3/5 * 4/5 = ", rational.get_fraction(), '=', rational.get_floating())
rational.div(2, 5)
print("12/25 / 2/5 = ", rational.get_fraction(), '=', rational.get_floating())

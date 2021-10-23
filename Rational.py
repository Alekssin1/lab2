from math import gcd


class Rational:

    def __init__(self, numerator=1, denominator=1):
        if isinstance(numerator, int) and isinstance(denominator, int):
            if denominator:
                self.__numerator = numerator
                self.__denominator = denominator

            else:
                raise ZeroDivisionError("Denominator can't be zero!")
        else:
            raise TypeError("Incorrect input! Variable type must be int!")

    @staticmethod
    def reduction(numerator, denominator):
        """ find greatest common divider of two integers and reduce fraction"""
        divider = gcd(numerator, denominator)
        return numerator // divider, denominator // divider

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        return Rational(numerator, denominator)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        denominator = self.__denominator * other.__denominator
        return Rational(numerator, denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        numerator = self.__numerator * other.__numerator
        denominator = self.__denominator * other.__denominator
        return Rational(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("It should be rational type!")
        if other.__numerator == 0:
            raise ZeroDivisionError("Division by zero!")
        numerator = self.__numerator * other.__denominator
        denominator = self.__denominator * other.__numerator
        return Rational(numerator, denominator)

    def get_fraction(self):
        """ return fraction in form numerator/denominator """
        reduce_form = self.reduction(self.__numerator, self.__denominator)
        return f"{int(reduce_form[0])}/{int(reduce_form[1])}"

    def get_floating(self):
        """ return fraction in floating-point format """
        return round(self.__numerator / self.__denominator, 2)


rational = Rational(3, 6)
print(f'3/6 = {rational.get_fraction()} = {rational.get_floating()}')
b = Rational(1, 5)
c = Rational(1, 10)
d = Rational(4, 5)
z = Rational(0, 3)
e = rational + b
print(f'{rational.get_fraction()} + {b.get_fraction()} = {e.get_fraction()} = {e.get_floating()}')
f = e - c
print(f'{e.get_fraction()} - {c.get_fraction()} = {f.get_fraction()} = {f.get_floating()}')
g = f * d
print(f'{f.get_fraction()} * {d.get_fraction()} = {g.get_fraction()} = {g.get_floating()}')
h = g / b
print(f'{g.get_fraction()} / {b.get_fraction()} = {h.get_fraction()} = {h.get_floating()}')
j = h / z
print(f'{h.get_fraction()} /  {z.get_fraction()} = {j.get_fraction()} = {j.get_floating()}')

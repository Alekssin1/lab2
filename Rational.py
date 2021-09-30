import math


class Rational:
    __numerator = 1
    __denominator = 1

    def __init(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if type(self.numerator) != int:
            print("Variable type must be int!!!")
            numerator = 1
            denominator = 1
        if self.denominator == 0:
            print("None")
            denominator = 1

    def reduction(self):
        if type(self.numerator / self.denominator) != 0:
            return self.numerator / math.gcd(self.numerator, self.denominator), self.denominator / math.gcd(
                self.numerator, self.denominator)
        else:
            return self.numerator, self.denominator


rational = Rational(3, 6)
print(f"{int(rational.reduction()[0])}/{int(rational.reduction()[1])}")
print(rational.reduction()[0]/rational.reduction()[1])
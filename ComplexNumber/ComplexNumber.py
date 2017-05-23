import sys


class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.realPart = real
        self.imagPart = imaginary
        return

    def __add__(self, other):
        return ComplexNumber(self.realPart + other.realPart,
                             self.imagPart + other.imagPart)

    def __sub__(self, other):
        return ComplexNumber(self.realPart - other.realPart,
                             self.imagPart - other.imagPart)

    def __mul__(self, other):
        return ComplexNumber(self.realPart * other.realPart -
                             self.imagPart * other.imagPart,
                             self.realPart * other.imagPart +
                             other.realPart * self.imagPart)

    def __truediv__(self, other):
        down = other.realPart ** 2 + other.imagPart ** 2
        one = (self.realPart * other.realPart +
               self.imagPart * other.imagPart) / down
        two = (self.imagPart * other.realPart -
               self.realPart * other.imagPart) / down
        return ComplexNumber(one, two)

    def __str__(self):
        returningstr = ''
        if self.realPart != 0.0 and self.imagPart != 0.0:
            returningstr += "{0:.2f}".format(self.realPart)
            if self.imagPart > 0.0:
                returningstr += ' + ' + \
                                "{0:.2f}".format(self.imagPart) + 'i'
            else:
                returningstr += ' - ' + \
                                "{0:.2f}".format(abs(self.imagPart)) + 'i'
        elif self.imagPart == 0.0 and self.realPart != 0.0:
            returningstr += "{0:.2f}".format(self.realPart)
        elif self.realPart == 0.0 and self.imagPart != 0.0:
            returningstr += "{0:.2f}".format(self.imagPart) + 'i'
        else:
            returningstr += '0.00'
        return returningstr

for k in sys.stdin:
    print(eval(k))

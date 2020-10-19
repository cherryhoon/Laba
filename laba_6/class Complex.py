import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)  # сложение

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)     # віч

    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary,
                       self.real * no.imaginary + no.real * self.imaginary)

    def __truediv__(self, no):
        denominator = no.real ** 2 + no.imaginary ** 2
        return Complex((self.real * no.real + self.imaginary * no.imaginary) / denominator,
                       (self.imaginary * no.real - self.real * no.imaginary) / denominator)

    def abs(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        return f'({self.real}+{self.imaginary}i)'


if __name__ == '__main__':
    x = Complex(2, 1)
    y = Complex(5, 6)
    print(*map(str, [x + y, x - y, x * y, x / y, x.abs(), y.abs()]), sep='')
from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        self.numer = None
        self.denom = None

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        # sum of r1 = a1/b1 and r2 = a2/b2
        # (a1 * b2 + a2 * b1) / (b1 * b2)
        # a1/b1 + a2/b2
        # r1 + r2
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        # |r| = |a|/|b|
        return abs(self.numer / self.denom)

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass

class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        pass

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        return str(self._numerator)

    def get_denominator(self):
        return str(self._denominator)

    def get_fraction(self):
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

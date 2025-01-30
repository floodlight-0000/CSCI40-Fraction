class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        pass

    def gcd(a, b):
        if a < b:
            smaller_int = a
            larger_int = b
        else:
            smaller_int = b
            larger_int = a
        
        remainder = larger_int % smaller_int

        return gcd(smaller_int, remainder)


    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass
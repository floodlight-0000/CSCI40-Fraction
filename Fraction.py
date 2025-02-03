from math import gcd as math_gcd

class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        invalid = False

        if isinstance(numerator, str) and "/" in numerator and "." not in numerator and denominator == 1:

            int_list = numerator.strip().split("/")

            if len(int_list) > 2:
                invalid = True
            else:
                numerator, denominator = int_list
                try:
                    numerator = int(numerator)
                    denominator = int(denominator)
                except:
                    invalid = True

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass

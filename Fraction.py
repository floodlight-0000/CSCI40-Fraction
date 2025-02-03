class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        #TODO
        pass

    def gcd(a, b):
        if isinstance (a, Fraction):
            a = a.a

        if a == 0 or b == 0:
            return 0

        def get_gcd(a,b):
            if a == 0:
                return b
            return get_gcd(b % a, a)
        
        return get_gcd(a,b)
        
    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass

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
                    
        elif isinstance(numerator, str) or isinstance(denominator, str):
            invalid = True

        if invalid:
            numerator = 0
            denominator = 1

        self.a = numerator
        self.b = denominator

        if numerator % 1 != 0:
            self.a = 0
        if denominator == 0:
            self.b = 1    
            raise ZeroDivisionError

    
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

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
        return str(self.a)

    def get_denominator(self):
        return str(self.b)

    def get_fraction(self):
        quo, rem = divmod(self.a, self.b)
        
        if self.a == 0:
            return "0"

        if abs(self.a) > abs(self.b) and rem == 0:
            return str(quo)
        
        if abs(self.a) > abs(self.b):
            return str(self.a) + "/" + str(self.b)

        return self.get_lowest_form()

    def get_lowest_form(self):
        gcd = 0
        while gcd != 1:
            gcd = self.gcd(self.b)
            self.a = int(self.a / gcd)
            self.b = int(self.b / gcd)

        if self.b < 0:
            self.a = self.a * -1
            self. b = self.b * -1
            
        return str(self.a) + "/" + str(self.b)

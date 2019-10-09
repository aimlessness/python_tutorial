class Rational(object):
    @staticmethod
    def _gcd(a, b):
        '''(a, b) == (b, a % b)'''
        
        if b == 0:
            return a

        while b != 0:
            a, b = b, a % b

        return a

    def __init__(self, numerator, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        if denominator == 0:
            raise ZeroDivisionError

        if denominator < 0:
            self._numerator = -numerator
            self._denominator = -denominator
        else:
            self._numerator = numerator
            self._denominator = denominator

        gcd = Rational._gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // gcd
        self._denominator = self._denominator // gcd

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)

        return "{}/{}".format(self._numerator, self._denominator)

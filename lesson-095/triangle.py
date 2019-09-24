def canBeTriangle(a, b, c):
    def isNumeric(value):
        t = type(value)
        return t == int or t == long or t == float

    if not isNumeric(a) or not isNumeric(b) or not isNumeric(c):
        return False

    return a + b > c and a + c > b and b + c > a

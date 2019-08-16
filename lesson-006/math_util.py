import types

def gcd(m, n):
    '''Calculate the gcd of m and n.
    Both m and n must be integer, and m,n > 0.
    For invalid m or n, return None.
    '''

    if not type(m) is types.IntType or not type(n) is types.IntType:
        return None

    if m <= 0 or n <= 0:
        return None

    max, min = m, n
    if max < min:
        max, min = min, max

    while True:
        if max == min:
            return max

        remainder = max % min
        if remainder == 0:
            return min

        max, min = min, remainder

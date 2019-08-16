#!/usr/bin/env python

import math_util

testcases = [
    (5, 17, 1), 
    (17, 5, 1), 
    (2, 4, 2),
    (6, 3, 3),
    (6.0, 3, None),
    (6, '3', None),
    (-6, 3, None),
    (6, -3, None),
    ]

for m, n, g in testcases:
    real = math_util.gcd(m, n)
    if real == g:
        print "PASS: ({m}, {n}, {g})".format(m=m, n=n, g=g)
    else:
        print "FAIL: ({m}, {n}, {g}) - {real}".format(m=m, n=n, g=g, real=real)

a = 1234568438124
b = 439181342313142344
gcd = math_util.gcd(a, b)
print 'gcd({a}, {b}) = {gcd}'.format(a=a, b=b, gcd=gcd)

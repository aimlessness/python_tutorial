#!/usr/bin/env python

import triangle

test_data = [
    ((3, 3, 3), True),
    ((3, 4, 5), True),
    ((.3, .4, .5), True),
    ((33.01, 44, 55), True),
    ((33333333333, 44444444444, 55555555555), True),
    ((-3, -4, -5), False),
    ((1, 2, 3), False),
    ((1, 2, 4), False),
    (('3', 4, 5), False),
    ((3, '4', 5), False),
    ((3, 4, '5'), False),
    ((None, None, None), False),
]

for edges, expect in test_data:
    a, b, c = edges
    real = triangle.canBeTriangle(a, b, c)
    if real == expect:
        print "PASS: ({a}, {b}, {c})=>{real}".format(
            a = a, b = b, c = c, real = real)
    else:
        print "FAIL: ({a}, {b}, {c}) => {real}, expect: {expect}".format(
            a = a, b = b, c = c, real = real, expect = expect)

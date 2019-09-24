#!/usr/bin/env python

import types

def foo(m, n):
    def isIntOrLong(value):
        return type(value) is types.IntType or type(value) is types.LongType

    if not isIntOrLong(m) or not isIntOrLong(n):
        return None

    # Calculating the gcd...
    return 1

def bar(m, n):
    if not (type(m) is types.IntType or type(m) is types.LongType) or \
        not (type(n) is types.IntType or type(n) is types.LongType):
        return None

    # Calculating the gcd...
    return 1

def baz(m, n):
    if (type(m) is not types.IntType and type(m) is not types.LongType) or \
        (type(n) is not types.IntType and type(n) is not types.LongType):
        return None

    # Calculating the gcd...
    return 1


testcases = [
    (5, 17, 1), 
    (5555555555555555, 17777777777777777, 1), 
    (5, 17777777777777777, 1),
    (17777777777777777, 5, 1),
    
    ('5', 17, None), 
    (5, '17', None), 
    ('5555555555555555', 17777777777777777, None), 
    (5555555555555555, '17777777777777777', None), 
    ('5', '17777777777777777', None),
    ]

for m, n, expect in testcases:
    for f in [foo, bar, baz]:
        real = f(m, n)
        if real == expect:
            print "PASS: {func_name}({m}, {n}) => {real})".format(func_name=f.func_name, m=m, n=n, real=real)
        else:
            print "FAIL: {func_name}({m}, {n}), expect: {expect}, real: {real}) - {real}".format(
                func_name=f.func_name, m=m, n=n, expect=expect, real=real)
    print
    

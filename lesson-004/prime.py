#!/usr/bin/env python

import sys
import math

def is_prime(n):
    max = int(math.sqrt(n))
    if n < 2:
        return False

    for i in range(2, max + 1):
        if n % i == 0:
            return False

    return True

if len(sys.argv) != 2:
    print 'Usage: {program} <n>'.format(program = sys.argv[0])
    sys.exit(1)
    
n = sys.argv[1]
if not n.isdigit():
    print 'Error: n must be a number.'
    sys.exit(1)

n = int(n)
for i in range(n + 1):
    if is_prime(i):
        print i,

print
print 'DONE.'

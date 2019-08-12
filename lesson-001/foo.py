#!/usr/bin/env python

import string 
import sys 

def add(a, b):
    return a + b

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "ERROR: Usage %s a b" % (sys.argv[0])
        sys.exit(1)

    print sys.argv[1]

    a = string.atoi(sys.argv[1])
    b = string.atoi(sys.argv[2], 10)
    ret = add(a, b)
    print "result:", ret

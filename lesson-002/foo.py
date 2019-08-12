#! /usr/bin/env python

import sys
import string

def  f(x,y):
    print (x+y)*(x-y)-x*x+y*y

if __name__ == '__main__':
    print 'argv count:', len(sys.argv)

    if len(sys.argv)!= 3:
        print 'Error!'
        sys.exit(1)
    
    a = string.atoi(sys.argv[1])
    b = string.atoi(sys.argv[2])

    f(a, b)

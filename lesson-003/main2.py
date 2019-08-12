#!/usr/bin/env python

import sys, string

import add
import minus

count = len(sys.argv)
if count != 4:
    print "Error: count is not 4"
    sys.exit(1)

op = sys.argv[1]
x = string.atoi(sys.argv[2])
y = string.atoi(sys.argv[3])

if op == 'add':
   print add.add(x,y)
   sys.exit(0)

elif op == 'minus':
   print minus.minus(x,y)
   sys.exit(0)

else:
   print 'op must be add or minus'
   sys.exit(1)

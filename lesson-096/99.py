#!/usr/bin/env python

for i in range(1, 10):
    for j in range(1, i + 1):
        print " %d x %d = %2d" % (i, j, i * j),
    print


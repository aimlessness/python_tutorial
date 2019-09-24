#!/usr/bin/env python

def multi_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print "%d x %d = %2d  " % (j, i, i * j),
        print

multi_table()

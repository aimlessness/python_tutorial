#!/usr/bin/env python

import datetime
import time
import sys

def permuations(values):
    if len(values) == 2:
        return [values[:], [values[1], values[0]]]

    if len(values) < 2:
        print "Error"
        return None

    allResults = []
    for i in range(len(values)):
        temp = values[:]
        temp[0], temp[i] = temp[i], temp[0]
        results = permuations(temp[1:])
        for item in results:
            item.insert(0, temp[0])
            allResults.append(item)

    return allResults

if len(sys.argv) != 2:
    print 'Usage: %s <n>\n\tn: 2~25' % (sys.argv[0])
    sys.exit(1)

'''
3 x 3, index from 0:
0 1 2
3 4 5
6 7 8

4 x 4:
 0  1  2  3
 4  5  6  7
 8  9 10 11
12 13 14 15
'''
def check_and_output(n, values, magic_sum):
    count = n * n
    if len(values) != count:
        print 'Error: length of values != n'
        return

    # check rows
    for row in range(n):
        if sum(values[row * n: row * n + n]) != magic_sum:
            #print 'row not match:', row
            return

    # check columns
    def remainder(r):
        return lambda x: x % 3 == r
    for column in range(n):
        if sum([values[i] for i in filter(remainder(column), range(count))]) != magic_sum:
            #print 'column not match:', column
            #print filter(remainder(column), values)
            return

    # check diagonals
    def diagonal(n):
        return [range(0, n * n, n + 1), range(n - 1, n * n - 1, n - 1)]
    diagonals = diagonal(n)
    if sum([values[i] for i in diagonals[0]]) != magic_sum:
        #print 'diagonals[0] not match'
        return
    if sum([values[i] for i in diagonals[1]]) != magic_sum:
        #print 'diagonals[1] not match'
        return
    
    for i in range(n):
        for j in range(n):
            print "%2d " % (values[i * n + j],),
        print
    print
    

#check_and_output(3, [2, 7, 6, 9, 5, 1, 4, 3, 8], 15)
#sys.exit(0)

start_time = datetime.datetime.now()
n = int(sys.argv[1])
print 'n:', n
base = [i for i in range(1, n * n + 1)]
magic_sum = sum(range(1, n * n + 1)) / n
print 'base:', base
results = permuations(base)
for item in results:
    #print 'item:', item
    check_and_output(n, item, magic_sum)

end_time = datetime.datetime.now()
delta = end_time - start_time
delta_gmtime = time.gmtime(delta.total_seconds())
duration = time.strftime("%H:%M:%S", delta_gmtime) 
print 'Spent time:', duration
print 'END'
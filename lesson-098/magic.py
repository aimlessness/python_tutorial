#!/usr/bin/env python
import sys
import datetime
import time

def check_and_output(n, count, magic_sum, values):
    length = len(values)

    if length < n:
        return True

    # check rows
    for row in range(int(length / n)):
        if sum(values[row * n: row * n + n]) != magic_sum:
            #print 'row not match:', row
            return False

    if length <= n * (n - 1):
        return True

    # check columns
    def remainder(r):
        return lambda x: x % n == r
    for column in range(length - n * (n - 1)):
        if sum([values[i] for i in filter(remainder(column), range(count))]) != magic_sum:
            #print 'column not match:', column
            #print filter(remainder(column), values)
            return False

    # check diagonals
    def diagonal(n):
        return [range(0, n * n, n + 1), range(n - 1, n * n - 1, n - 1)]
    diagonals = diagonal(n)

    if sum([values[i] for i in diagonals[1]]) != magic_sum:
        #print 'diagonals[1] not match'
        return False
    
    if length < count:
        return True

    if sum([values[i] for i in diagonals[0]]) != magic_sum:
        #print 'diagonals[0] not match'
        return False

    for i in range(n):
        for j in range(n):
            print "%2d " % (values[i * n + j],),
        print
    print
    return True

'''
count = n * n
'''
def magics(n, count, magic_sum, current, left):
    #print "   " * len(current), "current: {current}, left: {left}".format(current=current, left=left)
    if len(current) == count:
        check_and_output(n, count, magic_sum, current)
        return

    for i in range(len(left)):
        temp_current = current[:]
        temp_left = left[:]
        #print "   " * len(current), "try [%d] -> %d" % (i, left[i])
        temp_current.append(temp_left.pop(i))
        #print "   " * len(current), "temp current: {temp_current}, left: {temp_left}".format(
        #    temp_current = temp_current, temp_left = temp_left)
        if check_and_output(n, count, magic_sum, temp_current):
            if len(temp_current) < count:
                magics(n, count, magic_sum, temp_current, temp_left)

#check_and_output(3, 9, 15, [2, 7, 6, 9, 5, 1, 4, 3, 8])
#sys.exit(0)

if len(sys.argv) != 2:
    print 'Usage: %s <n>' % (sys.argv[0],)
    sys.exit(1)

start_time = datetime.datetime.now()
n = int(sys.argv[1])

magic_sum = sum(range(1, n * n + 1)) / n
current = []
left = [i for i in range(1, n * n + 1)]
magics(n, n * n, magic_sum, current, left)

end_time = datetime.datetime.now()
delta = end_time - start_time
delta_gmtime = time.gmtime(delta.total_seconds())
duration = time.strftime("%H:%M:%S", delta_gmtime) 
print 'Spent time:', duration
print 'END'
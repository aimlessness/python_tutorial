#!/usr/bin/env python

import sys
import datetime
import time

def permuations(n):
    if n <= 1 or n > 25:
        return None

    if n == 2:
        return [[1, 2], [2, 1]]

    results = permuations(n - 1)
    results2 = []
    for item in results:
        for i in range(n - 1, -1, -1):
            temp = item[:]
            temp.insert(i, n)
            results2.append(temp)

    return results2

if len(sys.argv) != 2:
    print 'Usage: %s <n>\n\tn: 2~25' % (sys.argv[0])
    sys.exit(1)

start_time = datetime.datetime.now()

results = permuations(int(sys.argv[1]))
for i in results:
    pass #print i

end_time = datetime.datetime.now()
delta = end_time - start_time
delta_gmtime = time.gmtime(delta.total_seconds())
duration = time.strftime("%H:%M:%S", delta_gmtime) 
print 'Time spent:', duration

print 'END'
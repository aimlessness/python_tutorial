#!/usr/bin/env python

import datetime
import time

'''
a1 a2 a3
a4 a5 a6
a7 a8 a9
'''
def check_and_output(a1, a2, a3, a4, a5, a6, a7, a8, a9):
    #print a1, a2, a3, a4, a5, a6, a7, a8, a9
    values = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
    for i in range(9):
        for j in range(i + 1, 9):
            if values[i] == values[j]:
                return

    sum = 15
    if not (a1 + a2 + a3 == sum and a4 + a5 + a6 == sum and a7 + a8 + a9 == sum and
        a1 + a4 + a7 == sum and a2 + a5 + a8 == sum and a3 + a6 + a9 == sum and
        a1 + a5 + a9 == sum and a3 + a5 + a7 == sum):
        return

    print "%2d %2d %2d\n%2d %2d %2d\n%2d %2d %2d\n" % (a1, a2, a3, a4, a5, a6, a7, a8, a9)

start_time = datetime.datetime.now()
for a1 in range(1, 10):
    for a2 in range(1, 10):
        for a3 in range(1, 10):
            for a4 in range(1, 10):
                for a5 in range(1, 10):
                    for a6 in range(1, 10):
                        for a7 in range(1, 10):
                            for a8 in range(1, 10):
                                for a9 in range(1, 10):
                                    check_and_output(a1, a2, a3, a4, a5, a6, a7, a8, a9)

end_time = datetime.datetime.now()
delta = end_time - start_time
delta_gmtime = time.gmtime(delta.total_seconds())
duration = time.strftime("%H:%M:%S", delta_gmtime) 
print 'Spent time:', duration
print 'END'

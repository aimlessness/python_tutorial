#!/usr/bin/env python

import add

for x in range (10):
    for y in range (10):
        print '{x} + {y} = {sum}'.format(
            x=x, y=y, sum=add.add(x,y))

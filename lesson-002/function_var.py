#! /usr/bin/env python

import sys
import string

def foo():
    print "foo"

def bar():
    print "bar"

if len(sys.argv) != 2:
    print 'Error!'
    sys.exit(1)

name = sys.argv[1]
f = None
if name == "foo":
    f = foo
elif name == "bar":
    f = bar
else:
    print "invalid name:", name
    sys.exit(1)

f()
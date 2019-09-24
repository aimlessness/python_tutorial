#!/usr/bin/env python

import magic

for n in range(10):
	print "n:", n
	m = magic.generate_magic(n)
	magic.print_magic(m)

print 'DONE!'

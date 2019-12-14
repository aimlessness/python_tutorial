#!/usr/bin/env python3

if False:
    print("1: unreachable")
else:
    print("2: goes here")

if 3 == 5:
    print("3: unreachable")
else:
    print("4: goes here")

a = None
if a:
    print("5: unreachable")
else:
    print("6: goes here")

a = [1]
if a:
    print("7: goes here")
else:
    print("8: unreachable")

if 0:
    print("9: unreachable")
else:
    print("10: goes here")

if 2:
    print("11: goes here")
else:
    print("12: unreachable")

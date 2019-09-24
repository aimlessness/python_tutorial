#!/usr/bin/env python

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def listPrimes(n):
    for i in range(n):
        if isPrime(i):
            print i,

    print

listPrimes(100)

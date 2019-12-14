#!/usr/bin/env python3

def fib(n):
    if n <= 0:
        raise ValueError("n must be greater than 0.")

    if n == 1 or n == 2:
        return 1
        
    return fib(n - 1) + fib(n - 2)

def sigma(n):
    if n <= 0:
        raise ValueError("n must be greater than 0.")

    return int(n * (n + 1) / 2)

if __name__ == '__main__':
    for n in range (0, 11):
        try:
            print(fib(n), end=" ")
        except Exception as e:
            print("n={}, Exception={}".format(n, e))
    print()

    for n in range (0, 11):
        try:
            print(sigma(n), end=" ")
        except Exception as e:
            print("n={}, Exception={}".format(n, e))
    print


```python
#!/usr/bin/env python

# [0, 1, 2, ..., 8]
values = range(9)

def remainder_0(n):
    return n % 3 == 0

def remainder_1(n):
    return n % 3 == 1

def remainder_2(n):
    return n % 3 == 2

sub_values_0 = filter(remainder_0, values)
sub_values_1 = filter(remainder_1, values)
sub_values_2 = filter(remainder_2, values)

print "0:", sub_values_0 # 0: [0, 3, 6]
print "1:", sub_values_1 # 1: [1, 4, 7]
print "2:", sub_values_2 # 2: [2, 5, 8]

# lambda expression
def remainder(r):
    return lambda x: x % 3 == r

'''
0: [0, 3, 6]
1: [1, 4, 7]
2: [2, 5, 8]
'''
for i in range(3):
    sub_values = filter(remainder(i), values)
    print "{i}: {sub_values}".format(i = i, sub_values = sub_values)
```

# class

```python

'''
0: [0, 3, 6]
1: [1, 4, 7]
2: [2, 5, 8]
'''
class Remainder(object):
    def __init__(self, r):
        self.r = r

    def __call__(self, x):
        return x % 3 == self.r

for i in range(3):
    sub_values = filter(Remainder(i), values)
    print "{i}: {sub_values}".format(i = i, sub_values = sub_values)
```

python - lambda

```python
#!/usr/bin/env python

# https://docs.python.org/zh-cn/2.7/tutorial/controlflow.html
def make_incrementor(n):
    def foo(x):
        return x + n

    return foo

foo = make_incrementor(42)
print "foo..."
for value in [0, 10, 20]:
    print "{value}=>{result}".format(value=value, result=foo(value))

class incrementor(object):
    def __init__(self, n):
        self.n = n

    def add(self, x):
        return x + self.n

    def __call__(self, x):
        return x + self.n

print "bar..."
bar = incrementor(42)
for value in [0, 10, 20]:
    print "{value}=>{result}".format(value=value, result=bar(value))

for value in [5, 15, 25]:
    print "{value}=>{result}".format(value=value, result=bar.add(value))
```

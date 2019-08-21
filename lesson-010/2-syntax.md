# 语法部分

## sum

doc:

```
sum(...)
    sum(iterable[, start]) -> value
    
    Return the sum of an iterable or sequence of numbers (NOT strings)
    plus the value of 'start' (which defaults to 0).  When the sequence is
    empty, return start.
```

example:
```python
>>> sum([1, 2])
3
>>> sum([1, 2, 3])
6
>>> sum(range(1, 11))
55
>>> 
```

## filter

```python
>>> values = range(9)
>>> values
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> def f(x):
...     return x % 3 == 0
... 
>>> filter(f, values)
[0, 3, 6]
>>> 
>>> def boo(x):
...     return x % 3 == 1
... 
>>> filter(boo, values)
[1, 4, 7]
>>> 
```

## lambda

另见 lambda.md.

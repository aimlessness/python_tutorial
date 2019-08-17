# types

为了提高代码质量，通常需要对变量进行严格的数据类型检查。比如，一个函数，首先需要对函数入参做类型检查，对于非预期的数据类型都需要提示或返回错误。

以下是常见的一些数据类型。

## int type

```python
>>> import types
>>> a = 5
>>> type(a)
<type 'int'>
>>> type(a) is int
True
>>> type(a) is types.IntType
True
>>> type(a) is not types.IntType
False
>>> not type(a) is types.IntType
False
>>> b = '5'
>>> type(b) is not types.IntType
True
>>> 
```

## long type

```python
>>> import types
>>> a = 1234568438124
>>> a
1234568438124L
>>> type(a) is long
True
>>> type(a) is types.LongType
True
>>> 
```

## string

```python
>>> b = 'abc'
>>> type(b)
<type 'str'>
>>> type(b) is str
True
>>> type(b) is types.StringType
True
>>> 
```

## list

```python
>>> c = [1, 2, 3]
>>> type(c)
<type 'list'>
>>> type(c) is list
True
>>> type(c) is types.ListType
True
>>> 
```

## dict

```python
>>> 
>>> d = {"name": "Tom"}
>>> type(d)
<type 'dict'>
>>> type(d) is dict
True
>>> type(d) is types.DictType
True
>>> 
```

## tuple

```
>>> 
>>> e = (1, 2)
>>> type(e)
<type 'tuple'>
>>> type(e) is tuple
True
>>> type(e) is types.TupleType
True
>>> 
```

## None

```python
>>> f = None
>>> type(f)
<type 'NoneType'>
>>> type(f) is types.NoneType
True
>>> f is None
True
>>> 
```

通常并不会判断 ```NoneType``` 类型，而直接用 ```is None``` 判断。

## function

```python
>>> def g():
    pass

>>> type(g)
<type 'function'>
>>> type(g) is function

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    type(g) is function
NameError: name 'function' is not defined
>>> type(g) is types.FunctionType
True
>>> 
```

# while loop

计算 1 ~ 10 之间各个整数的平方.

两种实现方式: for loop 和 while loop.

## for loop

```python
>>> for i in range(1, 11):
...     print "{a} * {b} = {c}".format(a=i, b=i, c=i*i)
...
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
6 * 6 = 36
7 * 7 = 49
8 * 8 = 64
9 * 9 = 81
10 * 10 = 100
>>>
```

## while loop

```python
>>> i = 1
>>> while i <= 10:
...     print "{a} * {b} = {c}".format(a=i, b=i, c=i*i)
...     i = i + 1
...
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
6 * 6 = 36
7 * 7 = 49
8 * 8 = 64
9 * 9 = 81
10 * 10 = 100
>>>
```

# continue & break

for 和 while 循环体内可以使用continue和break，其中break表示退出循环体，continue表示不再执行当前循环体内的剩余语句，而重新开始下一次循环。

## break

for loop:

```python
>>> for i in range(1, 100):
...     print "{a} * {b} = {c}".format(a=i, b=i, c=i*i)
...     i = i + 1
...     if i > 10:
...         break
...
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
6 * 6 = 36
7 * 7 = 49
8 * 8 = 64
9 * 9 = 81
10 * 10 = 100
>>>
```

while loop:

```python
>>> i = 1
>>> while True:
...     print "{a} * {b} = {c}".format(a=i, b=i, c=i*i)
...     i = i + 1
...     if i > 10:
...         break
...
1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
6 * 6 = 36
7 * 7 = 49
8 * 8 = 64
9 * 9 = 81
10 * 10 = 100
>>>
```

## continue

仅对 1 ~ 10 以内的偶数，计算其平方.

这里仅给出 for loop 中 continue 的例子；

```python
>>> for i in range(1, 11):
...     if i % 2 == 1:
...         continue
...     print "{a} * {b} = {c}".format(a=i, b=i, c=i*i)
...
2 * 2 = 4
4 * 4 = 16
6 * 6 = 36
8 * 8 = 64
10 * 10 = 100
>>>
```

当然，实际开发项目中会使用下面的方式:

```python
>>> for i in range(1, 11, 2):
...     print "{a} * {b} = {c}".format(a=i, b=i, c=i*i)
...
1 * 1 = 1
3 * 3 = 9
5 * 5 = 25
7 * 7 = 49
9 * 9 = 81
>>>
```

即使用带 step 的 range()。

# range

使用方法:

```
Help on built-in function range in module __builtin__:

range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers

    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.
```

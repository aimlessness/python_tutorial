# 语法

## 变量类型

```python

>>> type(1)
<type 'int'>
>>> type(1.0)
<type 'float'>
>>> type(111111111111111111111)
<type 'long'>
>>> type('1')
<type 'str'>
>>> 
```

## 布尔值及逻辑判断

```python
>>> a, b, c = 1, 2, 3
>>> a == b
False
>>> a > b
False
>>> a < b
True
>>> a + b == c
True
>>> a < b and b < c
True
>>> not a < b
False
>>> a is None
False
>>> a is not None
True
>>> 
```

## tuple

```python
>>> pointA = (1, 2)
>>> pointB = (3, 4)
>>> x_a, y_a = pointA
>>> x_b, y_b = pointB
>>> import math
>>> distance = math.sqrt((x_b - x_a)**2 + (y_b - y_a)**2)
>>> distance
2.8284271247461903
>>> 
```

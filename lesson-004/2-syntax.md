# list

定义、长度、索引。


```python
>>> a = [1, 2, 3, 4]
>>> len(a)
4
>>> a[0]
1
>>> a[2]
3
>>> a[3]
4
>>> a[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> a[-1]
4
>>> a[-4]
1
>>> a[-5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> 
```

# string

判断一个字符串是否为数字。

```python
>>> a = '123'
>>> a.isdigit()
True
>>> int(a)
123
>>> 
```

# math

```python
>>> import math
>>> math.sqrt(2)
1.4142135623730951
>>> 
```

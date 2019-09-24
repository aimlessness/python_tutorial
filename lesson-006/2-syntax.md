# list

## 定义、访问、切片(slice)

```python
>>> 
>>> a = [1, 2, 3, 4]
>>> len(a)
4
>>> a
[1, 2, 3, 4]
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
>>> 
>>> a[2:]
[3, 4]
>>> a[-2:]
[3, 4]
>>> a[-1:]
[4]
>>> a[1:-1]
[2, 3]
>>> 
>>> a[:]
[1, 2, 3, 4]
>>> 
```

## 两个列表相加

```python
>>> a
[1, 2, 3, 4]
>>> b = [5, 6, 7, 8]
>>> c = a + b
>>> c
[1, 2, 3, 4, 5, 6, 7, 8]
>>> 
```

## 修改列表中某个元素的值

```python
>>> a
[1, 2, 3, 4]
>>> a[1] = 20
>>> a
[1, 20, 3, 4]
>>> 
```

注意和元组(tuple)对比:

```python
>>> 
>>> point = (1, 2)
>>> point[0]
1
>>> point[0] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> 
```

## append, extend, insert, remove, pop, sort, reverse

```python
>>> a
[1, 2, 3, 4]
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> a.append(6, 7)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (2 given)
>>> a.append([6, 7])
>>> a
[1, 2, 3, 4, 5, [6, 7]]
>>> 
>>> 
>>> a.extend([8, 9])
>>> a
[1, 2, 3, 4, 5, [6, 7], 8, 9]
>>> a.remove(5)
>>> a
[1, 2, 3, 4, [6, 7], 8, 9]
>>> a.pop(4)
[6, 7]
>>> a
[1, 2, 3, 4, 8, 9]
>>> a.insert(4, 5)
>>> a
[1, 2, 3, 4, 5, 8, 9]
>>> a.insert(5, 6)
>>> a.insert(6, 7)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> a.reverse()
>>> a
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a.sort(reverse = True)
>>> a
[9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
>>> 
>>> 
```

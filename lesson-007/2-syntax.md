# list

## count, pop

```python
>>> b
[5, 6, 7, 8]
>>> b.extend([5, 6])
>>> b
[5, 6, 7, 8, 5, 6]
>>> b.count(5)
2
>>> b.count(6)
2
>>> b.count(7)
1
>>> b.pop()
6
>>> b
[5, 6, 7, 8, 5]
>>> b.pop()
5
>>> b
[5, 6, 7, 8]
>>> b.pop()
7
>>> b.pop()
6
>>> b.pop()
5
>>> b
[]
>>> b.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
>>> 
```

## List comprehensions

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
... 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> 
```


```python
>>> [(x, y) for x in range(5) for y in range(5) if x % 2 == 1 and y % 2 == 0]
[(1, 0), (1, 2), (1, 4), (3, 0), (3, 2), (3, 4)]
>>> 
```

等价于
```python
>>> combs = []
>>> for x in range(5):
...     for y in range(5):
...         if x % 2 == 1 and y % 2 == 0:
...             combs.append((x, y))
... 
>>> combs
[(1, 0), (1, 2), (1, 4), (3, 0), (3, 2), (3, 4)]
>>> 
```


```python
>>> vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
```

# 二维数组

数组中的每个元素还是一个数组。

## 示例1

```python
>>> magic = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
>>> type(magic)
<type 'list'>
>>> 
>>> magic
[[8, 1, 6], [3, 5, 7], [4, 9, 2]]
>>> 
>>> for row in magic:
...     for column in row:
...         print column,
...     print
... 
8 1 6
3 5 7
4 9 2
>>> for i in range(3):
...     for j in range(3):
...         print magic[i][j],
...     print
... 
8 1 6
3 5 7
4 9 2
>>> 
```

## 示例2

```python
>>> n = 3
>>> magic = [[x for x in range(n)] for y in range(n)]
>>> magic
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
>>> magic = [[0 for x in range(n)] for y in range(n)]
>>> magic
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>>
```

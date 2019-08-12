# lemda表达式

```python
>>> magic = [[x for x in range(n)] for y in range(n)]
>>> magic
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
>>> magic = [[0 for x in range(n)] for y in range(n)]
>>> magic
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>>
```

# 二维数组

数组中的每个元素还是一个数组。

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

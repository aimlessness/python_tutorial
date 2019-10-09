# 测验题

## 写出如下代码中，1\~6 处的执行结果.

### 代码1

```python
>>> b
[5, 6, 7, 8]
>>> b.extend([5, 6])
>>> b
# 1
>>> b.count(5)
# 2
>>> b.pop()
# 3
>>> b
# 4
```

## 代码2

```python
>>> a = [x**2 for x in range(5)]
>>> a
# 5
>>> [(x, y) for x in range(5) for y in range(5) if x % 2 == 1 and y % 2 == 0]
# 6
>>> vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> [num for elem in vec for num in elem]
# 7
>>> 
>>> n = 3
>>> magic = [[x for x in range(n)] for y in range(n)]
>>> magic
# 8
>>> 
```

## 阅读以下代码，并写出代码执行结果.

```python
def foo(n):
    a = 0
    for i in range(n + 1):
        a = a + i

    return a

def bar(n):
    a = 0
    for i in range(n + 1):
        if i % 2 == 1:
            a = a + i

    return a

print foo(10)
print bar(10)
```

# 测验题

## 写出如下代码中，1\~4 处的执行结果.

```python
>>> range(5)
# 1
>>> range(1, 5)
# 2
>>> range(1, 5, 2)
# 3
>>> [i * i for i in range(4)]
# 4
>>>
```

# 写出下面各程序的执行结果

## 程序1

```python
def foo(values):
    length = len(values)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if values[j] < values[i]:
                temp = values[i]
                values[i] = values[j]
                values[j] = temp

    return values

print foo([7, 1, 5, 3])
```

# 程序2

```python
def foo(values, target):
    if values is None or len(values) == 0:
        return -1

    high = len(values) - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if values[mid] == target:
            return mid

        if values[mid] < target:
            low = mid + 1
        elif values[mid] > target:
            high = mid - 1

    return -1

target = 5
for item in [
    None,
    [],
    [1],
    [5],
    [1, 5],
    [1, 3, 5, 7],
    [10, 30, 50, 70]
]:
    print foo(item, target),
print
```

## 优化以下代码

```python
import math

def foo(n):
    values = [True for i in range(n + 1)]
    values[0] = values[1] = False
    
    pos = 2
    while pos <= n:
        exists = False
        for i in range(pos, n + 1):
            if values[i]:
                pos = i
                exists = True
                break

        if not exists:
            break

        for i in range(pos + 1, n + 1):
            if i % pos == 0:
                values[i] = False

        pos = pos + 1

    ret = []
    for i in range(n + 1):
        if values[i]:
            ret.append(i)

    return ret

print foo(100)
```
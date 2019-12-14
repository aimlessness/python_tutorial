# 问题

分析以下两个 if 语句的差异:

```python
if n == 1 or n == 2:
    return 1

if n == 1 or 2:
    return 1
```

# 逻辑 True 和 False 的取值

## True, False

```python
if False:
    print("1: unreachable")
else:
    print("2: goes here")
```

## 逻辑判断条件为 False

```python

if 3 == 5:
    print("3: unreachable")
else:
    print("4: goes here")
```

## None 对应 False, not None 对应 True

```python
a = None
if a:
    print("5: unreachable")
else:
    print("6: goes here")

a = [1]
if a:
    print("7: goes here")
else:
    print("8: unreachable")
```

## 对于整数, 0 对应 False, 非 0 对应 True

```python
if 0:
    print("9: unreachable")
else:
    print("10: goes here")

if 2:
    print("11: goes here")
else:
    print("12: unreachable")
```

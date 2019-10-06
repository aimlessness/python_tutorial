# 测验题

## 写出如下代码中，1\~6 处的执行结果.

### 代码1

```python
a = [1, 2, 3, 4]
print(len(a)) # 1
print(a[0]) # 2
print(a[-1]) # 3

a.append(5)
a.insert(0, 6)
print(a) # 4

a = ['a', 'b']
a.extend(['c', ['d']])
print(a) # 5
```

### 代码2

```python
x = 1
y = 2
z = x * y
result = "%d x %d = %d" % (x, y, z)
print(result) # 6
```

## 请找出文件 is_prime.py 中的错误，并修改.

### is_prime.py

文件 is_prime.py 中定义了一个素数判定的函数:

```python
def is_prime(n):
    if n < 2:
        return True

    if n == 2 or n == 3:
        return True

    upper = int(math.sqrt())
    for i in range(upper):
        if n % i == 0:
            return False

    return True
```

### is_prime_test.py

文件 is_prime_test.py 调用 is_prime.py 中定义的函数，筛选出100以内的素数:

```python
import is_prime

for i in range(100):
    if is_prime.is_prime(i):
        print i,

print
print 'DONE'
```

## 阅读以下代码，并写出代码执行结果.

```python
def foo(m, n):
    if m <= 0 or n <= 0:
        return None

    max, min = m, n
    if max < min:
        max, min = min, max

    while True:
        if max == min:
            return max

        r = max % min
        if r == 0:
            return min

        max, min = min, r

print foo(4, 2)
print foo(4, 5)
print foo(4, 12)
```

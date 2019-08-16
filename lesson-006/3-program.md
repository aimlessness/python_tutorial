# 脚本文件

## math_util.py

从本节开始，我们将所有的 math 相关的函数都放到一个单独的文件 math_util.py 中，从而在后续的项目中可以重用已有的代码，避免重复开发。

在本节，需要实现计算两个正整数的最大公约数的算法，即 gcd(m, n).

## gcd_test.py

对这个函数的验证或测试，则放在 gcd_test.py 中。——暂时不用unittest。

# gcd (程序设计)

函数原型:

```python
def gcd(m, n):
    '''return the gcd of m and n.'''
    pass
```

计算两个正整数的最大公约数的方法如下。

## 输入

m, n

## 处理

- step 1: 如果 m < n, 则交换位置，即保证 m >= n.
- step 2: 如果 m == n, 则 m 或 n 即为最大公约数，返回该数. 否则，
- step 3: 计算余数 remainder = m % n;
- step 4: 如果 remainder 为0，则 n 为最大公约数，返回 n；否则，
- step 5: m, n = n, remainder, goto step 2.

## 输出

如果输入非法，返回 None; 否则，返回两数的最大公约数.

# 测试数据

在具体实现以上步骤之前，首先构造测试数据，以便于对待实现的 gcd() 函数进行测试。

按 (整数1, 整数2, 最大公约数) 的形式记录所有测试数据.

```python
testcases = [
    (5, 17, 1), 
    (17, 5, 1), 
    (2, 4, 2),
    (6, 3, 3),
    (6.0, 3, None),
    (6, '3', None),
    (-6, 3, None),
    (6, -3, None),
    ]
```

# 编码

## math_util.py

```python
def gcd(m, n):
    '''return the gcd of m and n.'''
    pass
```

## gcd_test.py

```python
#!/usr/bin/env python

import math_util

testcases = [
    (5, 17, 1), 
    (17, 5, 1), 
    (2, 4, 2),
    (6, 3, 3),
    (6.0, 3, None),
    (6, '3', None),
    (-6, 3, None),
    (6, -3, None),
    ]
for m, n, expect in testcases:
    real = math_util.gcd(m, n)
    if real == expect:
        # PASS
        pass
    else:
        # FAIL
        pass
```

在搭建以上文件&代码框架之后，就一点点丰富代码，最终让所有的测试用例都测试通过即可。

这个开发的过程，就是测试驱动开发(TDD, Test-Driven Development)。

# 参考代码

- [math_util.py](./math_util.py)
- [gcd_test.py](./gcd_test.py)

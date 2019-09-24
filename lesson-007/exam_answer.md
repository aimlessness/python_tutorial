# 参考答案

## 1\~6 打印结果

```
1. 4
2. 1
3. 4
4. [6, 1, 2, 3, 4, 5]
5. ['a', 'b', 'c', ['d']]
6. 1 x 2 = 2
```

## 代码找错

正确的代码:

```python
import math

def is_prime(n):
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    upper = int(math.sqrt(n))
    for i in range(2, upper + 1):
        if n % i == 0:
            return False

    return True
```

错误点:

1. 少了 ```import math```;
2. 当 ```if n<2``` 后面应该返回 ```False```;
3. 函数调用 ```sqrt()``` 中少了参数 ```n```;
4. ```range()```的参数有误，应该是 ```range(2, upper + 1)```;

## 代码执行结果

这个函数是计算两个大于0的自然数的最大公约数，答案是:

```2, 1, 4```
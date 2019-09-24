# program: 判断三边可否构成三角形

输入3条边的边长 a, b, c; 判断这三条边可否构成三角形，如果可以，返回True; 否则，返回False.

## 函数原型

```python
def canBeTriangle(a, b, c):
    pass
```

## 测试用例

测试数据

```
test_data = [
    ((3, 3, 3), True),
    ((3, 4, 5), True),
    ((.3, .4, .5), True),
    ((33.01, 44, 55), True),
    ((33333333333, 44444444444, 55555555555), True),
    ((-3, -4, -5), False),
    ((1, 2, 3), False),
    ((1, 2, 4), False),
    (('3', 4, 5), False),
    ((3, '4', 5), False),
    ((3, 4, '5'), False),
    ((None, None, None), False),
]
```

测试结果:

```
PASS: (3, 3, 3)=>True
PASS: (3, 4, 5)=>True
PASS: (0.3, 0.4, 0.5)=>True
PASS: (33.01, 44, 55)=>True
PASS: (33333333333, 44444444444, 55555555555)=>True
PASS: (-3, -4, -5)=>False
PASS: (1, 2, 3)=>False
PASS: (1, 2, 4)=>False
PASS: (3, 4, 5)=>False
PASS: (3, 4, 5)=>False
PASS: (3, 4, 5)=>False
PASS: (None, None, None)=>False
```

## 附: Code

- triangle.py
- triangle_test.py

## 思考

在已有的代码中，是否要添加 a, b, c 大于0 的判断？

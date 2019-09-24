# 奇数阶幻方

## 参考资料

[magicsquares-intro.html](http://www.math.wichita.edu/~richardson/mathematics/magic%20squares/magicsquares-intro.html)

## 需求

实现如下两个接口:

```python
def generate_magic(n):
    pass

def print_magic(magic):
    pass
```

其中:

- generate_magic(n): 输入一个奇数n，然后返回二维数组表示的幻方;
- print_magic(magic): 输入二维数组形式的magic，按照行列打印这个幻方.

## 分析与设计

### print_magic()

和前面的语法部分的示例代码类似，修改即可.

```python
def print_magic(magic):
    for row in magic:
        for column in row:
            print column,
        print
```

### generate_magic()

接下来重点分析幻方的生成算法。

## 算法

第一层分解:

```
1. 对输入参数进行合法性检查: 正数、奇数、大于1，不能太大（比如规定小于10）
2. 初始化二位数组
3. 按照奇数幻方的规则填数
```

前两点相对简单，主要是第三点，因此继续细化(第二层分解):

```
3.1 初始化: 
3.1.1 第一行的中间位置: row = 0, column = n / 2
3.1.2 当前已经填写的数字个数: count = 0
3.1.3 接下来要填写的数字: current_number = 1

循环执行以下各步骤:
3.2 在 (row, column) 位置填上 current_number;
3.3 count = count + 1; current_number = current_number + 1;
3.4 如果count == n * n，则填写结束，程序结束; 
3.4 移动位置:
3.4.1 如果count是n的倍数，则往下落，即 row = row + 1, column不变；否则，
3.4.2 往右上角方向走，即行号减一，列号加1: row = row - 1, column = column + 1; 并且，
3.4.2.1 如果 row == -1, 则row = n - 1 ; 如果column == n, 则 column = 0.
```

这里给出的是多次修正后的步骤，实际上，在这个过程中，会有多次反复的修改。

## Code

### magic.py

```python
def generate_magic(n):
    if not isinstance(n, int):
        print "Error: Not int"
        return None

    if n < 3 or n > 10:
        print "Error, must be [3, 10]"
        return None

    if n % 2 != 1:
        print "Error, must be odd."
        return None

    row = 0
    column = n / 2
    count = 0
    current_number = 1
    magic = [[0 for x in range(n)] for y in range(n)]

    while True:
        #print 'setting, row: {row}, column: {column}, number: {number}'.format(
        #    row=row, column=column, number=current_number)
        magic[row][column] = current_number
        
        count = count + 1
        current_number = current_number + 1

        if count == n * n:
            return magic

        if count % n == 0:
            row = row + 1
        else:
            row = row - 1
            column = column + 1
            if row == -1:
                row = n - 1
            if column == n:
                column = 0


def print_magic(magic):
    if not magic:
        print 'Not magic'
        return

    for row in magic:
        for column in row:
            print "%3d" % (column,),
        print
```

### magic_test.py

```python
#!/usr/bin/env python

import magic

for n in range(10):
    print "n:", n
    m = magic.generate_magic(n)
    magic.print_magic(m)

print 'DONE!'
```

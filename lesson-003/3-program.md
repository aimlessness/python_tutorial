# 需求

- 创建两个文件, add.py & minus.py, 其中分别定义两数加法和两数减法的函数;
- 创建main.py，根据命令行参数，调用add和minus模块中的函数
- main.py调用格式:

```
main.py <op> <a> <b>
```

其中，op 取值 add，表示对两数执行加法运算；取值 minus 表示对两数执行减法运算；其他均为非法运算符.

# 语法点

- 模块的概念
- import
- if-else
- command line arguments

# code

- add.py: 加法运算的函数定义
- minus.py: 减法运算的函数定义
- main.py, main2.py: 接受命令行参数，执行加减运算. 两个文件的区别仅在于if-else的写法不同。

# for loop 简介

语法:

- for loop
- string.format()

# 代码执行结果

```
$ ./main.py
Error: count is not 4

$ ./main.py add
Error: count is not 4

$ ./main.py add 2 3
5

$ ./main.py minus 2 3
-1

$ ./main.py div 2 3
op must be add or minus

$ ./for.py
0 + 0 = 0
0 + 1 = 1
0 + 2 = 2
...
9 + 4 = 13
9 + 5 = 14
9 + 6 = 15
9 + 7 = 16
9 + 8 = 17
9 + 9 = 18

$

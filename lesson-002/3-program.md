# Key

- function definition: 定义一个函数（平方差公式验证）
- command line arguments: 从命令行传入不同的数据进行验证

# Code

## foo.py

平方差公式的验证。

```
$ ./foo.py
argv count: 1
Error!

$ ./foo.py 1 2
argv count: 3
0

$ ./foo.py 1 2 3
argv count: 4
Error!

$
```

## function_var.py

函数变量简介。

output:
```
$ chmod +x f.py
$ ./f.py 
Error!
$ ./f.py foo
foo
$ ./f.py bar
bar
$ ./f.py baz
invalid name: baz
$ 
```

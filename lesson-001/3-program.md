通过脚本文件，定义一个加法运算，并可以通过命令行参数执行不同整数的加法。

对于foo.py中的细节部分，后续各讲逐步展开讨论。本讲能够通过对比了解交互式执行环境和命令行脚本文件执行方式的差异即可。

```
$ ./foo.py
ERROR: Usage ./foo.py a b

$ ./foo.py 2 3
2
result: 5

$ ./foo.py 20 5
20
result: 25

$
```
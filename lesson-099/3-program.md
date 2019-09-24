# 检查重复文件

检查指定目录下的重复文件（内容重复），并列出。

用户可指定最大重复文件个数，即达到该值后，就停止检索。

## API

```python

def checkRepeatedFiles(path, maxCount = 0):
    pass
```

maxCount缺省为0，表示检查所有的文件。

## 设计

因为是检查文件内容重复，所以这里计算每个文件的MD5，而且以MD5为key，其值为对应的文件列表。

同时为了计算当前已经重复的文件个数，简化为具有重复MD5的个数，所以另外一个列表用于计算重复MD5列表。

```python
class RepeatedFilesChecker(object):
    def __init__(self, path, maxCount = 0):
        self.repeatedMD5 = []
        self.md5Maps = {}
        self.path = path
        self.maxCount = maxCount

    def check(self):
        pass
```


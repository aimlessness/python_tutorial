# magic_test.py

magic_test.py用于驱动magic.py，对两个API进行验证(测试).

```
$ ./magic_test.py
n: 0
Error, must be [3, 10]
Not magic
n: 1
Error, must be [3, 10]
Not magic
n: 2
Error, must be [3, 10]
Not magic
n: 3
  8   1   6
  3   5   7
  4   9   2
n: 4
Error, must be odd.
Not magic
n: 5
 17  24   1   8  15
 23   5   7  14  16
  4   6  13  20  22
 10  12  19  21   3
 11  18  25   2   9
n: 6
Error, must be odd.
Not magic
n: 7
 30  39  48   1  10  19  28
 38  47   7   9  18  27  29
 46   6   8  17  26  35  37
  5  14  16  25  34  36  45
 13  15  24  33  42  44   4
 21  23  32  41  43   3  12
 22  31  40  49   2  11  20
n: 8
Error, must be odd.
Not magic
n: 9
 47  58  69  80   1  12  23  34  45
 57  68  79   9  11  22  33  44  46
 67  78   8  10  21  32  43  54  56
 77   7  18  20  31  42  53  55  66
  6  17  19  30  41  52  63  65  76
 16  27  29  40  51  62  64  75   5
 26  28  39  50  61  72  74   4  15
 36  38  49  60  71  73   3  14  25
 37  48  59  70  81   2  13  24  35
DONE!
```

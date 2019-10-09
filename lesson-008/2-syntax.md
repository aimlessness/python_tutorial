# class

文件 [student.py](https://github.com/aimlessness/python_tutorial/blob/master/lesson-008/student.py) 定义了一个 Student 类，包括两个属性: 名字和年龄. 

另外定了三个方法:

- name(), age(): 分别返回对象的名字和年龄;
- print(): 打印 Student 对象的信息.

运行:

```
$ python student.py
I'm Tom, I'm 10 years old.
I'm Jerry, I'm 9 years old.
Sum of Tom's and Jerry's age is 19
```

# unittest


文件 [student_test.py](https://github.com/aimlessness/python_tutorial/blob/master/lesson-008/student_test.py) 是针对 Student 类的一个示例测试用例. 

运行:

```
$ python student_test.py
I'm Tom, I'm 10 years old.
I'm Jerry, I'm 9 years old.
Sum of Tom's and Jerry's age is 19.
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

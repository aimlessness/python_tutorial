class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def name(self):
        return self._name

    def age(self):
        return self._age

    def print(self):
        msg = "I'm {}, I'm {} years old.".format(
            self._name, self._age)
        print(msg)

tom = Student('Tom', 10)
jerry = Student('Jerry', 9)
tom.print()
jerry.print()
print("Sum of {}'s and {}'s age is {}.".format(
    tom.name(), jerry.name(), tom.age() + jerry.age()))
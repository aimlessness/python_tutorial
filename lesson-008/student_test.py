from student import Student
import unittest

NAME = 'Tom'
AGE = 10

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(NAME, AGE)

    def test_name(self):
        self.assertEqual(self.student.name(), NAME)

    def test_age(self):
        self.assertEqual(self.student.age(), AGE)

if __name__ == '__main__':
    unittest.main()
    
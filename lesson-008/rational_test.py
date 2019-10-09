import unittest

from rational import Rational

class TestReq1(unittest.TestCase):
    def test_1_2(self):
        r = Rational(1, 2)
        self.assertEqual(str(r), "1/2")

    def test_2_1(self):
        r = Rational(2, 1)
        self.assertEqual(str(r), "2")
    
class TestReq2(unittest.TestCase):
    def test_3_9(self):
        r = Rational(3, 9)
        self.assertEqual(str(r), "1/3")

    def test_3_7(self):
        r = Rational(3, 7)
        self.assertEqual(str(r), "3/7")

class TestReq3(unittest.TestCase):
    def test_1_n2(self):
        r = Rational(1, -2)
        self.assertEqual(str(r), "-1/2")

    def test_n1_n2(self):
        r = Rational(-1, -2)
        self.assertEqual(str(r), "1/2")

    def test_n4_2(self):
        r = Rational(-4, 2)
        self.assertEqual(str(r), "-2")

class TestReq4(unittest.TestCase):
    def test_1_0(self):
        try:
            r = Rational(1, 0)
        except ZeroDivisionError:
            pass
        except Exception as e:
            self.assertTrue(False, "unexpected exception: {}".format(e))
        else:
            self.assertTrue(False, "No exception occur!")

class TestReq5(unittest.TestCase):
    def test_values(self):
        for p, q in [(1.0, 2), (1, 2.0), ("1", 2), ("1", "2"), (1, "2")]:
            try:
                r = Rational(p, q)
            except TypeError:
                pass
            except Exception as e:
                self.assertTrue(False, "unexpected exception: {}".format(e))
            else:
                self.assertTrue(False, "No exception occur!")

class TestReq6(unittest.TestCase):
    def test_values(self):
        for p, expect in [(1, "1"), (-2, "-2")]:
            r = Rational(p)
            self.assertEqual(str(r), expect)

if __name__ == '__main__':
    unittest.main()

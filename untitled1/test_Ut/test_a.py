import sys
sys.path.append("C:\\Users\\Administrator\\PycharmProjects\\untitled1")
import unittest
from test_Ut.a import *





class test_ss(unittest.TestCase):
    def test_add(self):
        self.assertEqual(3,add(1, 2))
        self.assertNotEqual(3,add(2, 2))



    def test_minus(self):
        self.assertEqual(1, minus(3, 2))




    def test_multi(self):
        self.assertEqual(6, multi(2, 3))



    def test_divide(self):
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
        unittest.main()

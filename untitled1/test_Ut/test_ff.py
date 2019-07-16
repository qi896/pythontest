import unittest




class test_temp(unittest.TestCase):
    def testss(self):
        a = 3
        b = 5
        self.assertNotEqual(a,b)
        print("testss")



    def testrr(self):
        a = "we"
        b = "we"
        self.assertEqual(a,b)
        print("2")



    def testth(self):
        a = "dss"
        b = 5
        self.assertNotEqual(a,b)
        print("3")



    def testfo(self):
        a = "sadfsdf"
        b = "dsfsf"
        self.assertNotEqual(a,b)
        print("4")


if __name__ == '__main__':
    unittest.main()

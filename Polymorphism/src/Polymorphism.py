import unittest


class Test(unittest.TestCase):

    def testPolymorphism(self):
        str1 = "Hello, "
        str2 = "World!"
        self.assertEqual(str1 + str2, "Hello, World!")
        
        num1 = 40
        num2 = 2
        self.assertEqual(num1 + num2, 42)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

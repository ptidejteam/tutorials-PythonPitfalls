import unittest


class Test(unittest.TestCase):

    def testLambda1(self):
        l = lambda x: x + 1
        self.assertEqual(l(1), 2)

    def testLambda2(self):
        l = lambda a, b: a * b
        self.assertEqual(l(2, 3), 6)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

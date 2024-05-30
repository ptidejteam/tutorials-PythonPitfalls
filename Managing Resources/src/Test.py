# https://www.geeksforgeeks.org/with-statement-in-python/

import unittest
from WithStatement import A


class Test(unittest.TestCase):

    def testBad(self):
        file = open('log1.txt', 'w')
        file.write('hello world !')
        file.close()

    def testGood(self):
        file = open('log2.txt', 'w')
        try:
            file.write('hello world')
        finally:
            file.close()

    def testBetter(self):
        with open('log3.txt', 'w') as file:
            file.write('hello world !')

    def testUserDefined(self):
        with A() as a:
            self.assertEqual(a.foo(), 42)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

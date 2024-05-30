import unittest
from pathlib import Path
from Decorators import greet, summator, summator2, A


class Test(unittest.TestCase):

    def testAddMessageToFunction(self):
        self.assertEqual(greet(), "Intercepted: Hello, world!, returning Bye!")

    def testAddMessageToMethod(self):
        a = A()
        self.assertEqual(a.greet(), "Intercepted: Hello, world!, returning Bye!")
        
    def testLogger(self):
        self.assertEqual(summator([1, 2, 3, 4, 5]), 15)
        log_file = Path("log.txt")
        self.assertTrue(log_file.is_file())

    def testLogger2(self):
        self.assertEqual(summator2([1, 2, 3, 4, 5]), 15)
        log_file = Path("log.txt")
        self.assertTrue(log_file.is_file())


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

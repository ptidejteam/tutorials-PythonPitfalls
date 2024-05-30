import unittest
import time


class Test2(unittest.TestCase):

    def testComprehension(self):
        start = time.time()
        result = [i for i in range(10000000)]
        end = time.time()
        time_diff = end - start
        
        self.assertEqual(len(str(result)), 88888890)
        self.assertTrue(time_diff > 0.5)  # Seconds

    def testGenerator(self):
        start = time.time()
        result = (i for i in range(10000000))
        end = time.time()
        time_diff = end - start

        result = list(result)

        self.assertEqual(len(str(result)), 88888890)
        self.assertTrue(time_diff < 0.1)  # Seconds


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

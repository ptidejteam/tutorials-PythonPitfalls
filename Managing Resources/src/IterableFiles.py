import unittest
import _io


class Test(unittest.TestCase):

    def testIterableFiles(self):
        result = open("Roy's Last Words") 
        self.assertEqual(type(result), _io.TextIOWrapper)
        result2 = []
        for l in result:
            result2 += [l]
        self.assertEqual(len(result2), 7)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

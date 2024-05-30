# https://stackoverflow.com/questions/2175080/sscanf-in-python

import unittest
from parse import parse


class Test(unittest.TestCase):

    def testParser1(self):
        result = parse('{} fish', '1')
        self.assertEqual(result, None)

    def testParser2(self):
        result = parse('{}', '1')
        self.assertEqual(result[0], '1')

    def testParser3(self):
        result = parse('{}, World!', 'Hello, World!')
        self.assertEqual(result[0], 'Hello')

    def testParser4(self):
        result = parse('{}, {}!', 'Hello, World!')
        self.assertEqual(result[0], 'Hello')
        self.assertEqual(result[1], 'World')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

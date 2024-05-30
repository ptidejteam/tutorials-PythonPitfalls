import unittest


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.l = [1, 2, 3]

    def testAppending(self):
        self.l[len(self.l):] = [4]
        self.assertEqual(self.l, [1, 2, 3, 4])

    def testPrepending(self):
        self.l[:0] = [0]
        self.assertEqual(self.l, [0, 1, 2, 3])

    def testReplacing(self):
        self.l[:2] = ['a', 'b', 'c']
        self.assertEqual(self.l, ['a', 'b', 'c', 3])

    def testInserting(self):
        self.l[2:2] = ['a', 'b']
        self.assertEqual(self.l, [1, 2, 'a', 'b', 3])


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

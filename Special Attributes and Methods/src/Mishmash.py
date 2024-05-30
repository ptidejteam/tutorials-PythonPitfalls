import unittest


class Test(unittest.TestCase):

    def testMishmash(self):
        x = [0, 1, 4, 3, 2, 1]
        
        self.assertEqual(x.count(1), 2)
        self.assertEqual(len(x), 6)
        self.assertTrue(isinstance(any(x), int))
        
        self.assertEqual(x[0], 0)
        x.reverse()
        self.assertEqual(x[0], 1)
        
        self.assertEqual(x[0], 1)
        x2 = list(reversed(x))
        self.assertEqual(x2[0], 0)

        x.sort()
        self.assertEqual(x[0], 0)
        self.assertEqual(x[1], 1)
        self.assertEqual(x[5], 4)

        x2 = list(sorted(x))
        self.assertEqual(x2[0], 0)
        self.assertEqual(x2[1], 1)
        self.assertEqual(x2[5], 4)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

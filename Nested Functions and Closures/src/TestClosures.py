import unittest


def multiplier(factor):
    f = factor * 2

    def multiply(x):
        nonlocal f
        return x * f

    return multiply


class Test(unittest.TestCase):

    def testDouble(self):
        double = multiplier(2)
        self.assertEqual(double(10), 40)
        self.assertEqual(double(20), 80)

    def testTriple(self):
        double = multiplier(3)
        self.assertEqual(double(10), 60)
        self.assertEqual(double(20), 120)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

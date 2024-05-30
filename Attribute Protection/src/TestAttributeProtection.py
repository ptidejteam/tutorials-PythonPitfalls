# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

import unittest
from Inheritance import A, C, _Z


class Test(unittest.TestCase):

    def testZ(self):
        z = _Z()
        self.assertEqual(z.__dict__.__len__(), 3)
        self.assertTrue(isinstance(z._B__z, int))

    def testA(self):
        a = A()
        self.assertEqual(a.__dict__.__len__(), 2)
        self.assertTrue(isinstance(a.x, int))
        self.assertTrue(isinstance(a._y, int))

    def testC(self):
        c = C()
        self.assertEqual(c.__dict__.__len__(), 3)
        self.assertTrue(isinstance(c._B__z, int))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

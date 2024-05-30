import unittest
from ImmutableDataClass import ImmutableDataClass, ImmutableClass
from VariableDeclaration import A
from typing import Final
import dataclasses


class Test(unittest.TestCase):

    def testConstant(self):
        # Final is just an annotation for a type checker
        MAX_SPEED: Final[int] = 300
        self.assertEqual(MAX_SPEED, 300)
        MAX_SPEED = 500
        self.assertEqual(MAX_SPEED, 500)  # Cannot assign to final name "MAX_SPEED" mypy(error)

    def testMutableParameters(self):
        a = A()
        l = []
        a.foo3('Hello', l)
        self.assertEqual(len(l), 1)
        a.foo3('World', l)
        self.assertEqual(len(l), 2)
    
    def testImmutableParameters(self):
        a = A()
        l = []
        try:
            a.foo3('Hello', frozenset(l))
            self.assertEqual(len(l), 1)
        except AttributeError:
            self.assertTrue(True)
        try:
            a.foo3('World', frozenset(l))
            self.assertEqual(len(l), 2)
        except AttributeError:
            self.assertTrue(True)
    
    def testImmutableDataClass(self):
        idc = ImmutableDataClass(1, 2)
        self.assertEqual(idc.a, 1)
        self.assertEqual(idc.b, 2)
        try:
            idc.a = 42
        except dataclasses.FrozenInstanceError:
            self.assertTrue(True)

    def testImmutableClass(self):
        try:
            ic = ImmutableClass(1, 2)
            self.assertEqual(ic.a, 1)
            self.assertEqual(ic.b, 2)
            ic.foo()
            self.assertEqual(ic.a, 2)
        except dataclasses.FrozenInstanceError:
            self.assertTrue(True)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

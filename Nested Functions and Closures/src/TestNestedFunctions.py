import unittest
from NestedFunctions import A, foo


class Test(unittest.TestCase):

    def testNestedFunctionLocalShadow(self):
        a = A()
        self.assertEqual(a.foo1(), 1)

    def testNestedFunctionNonLocal(self):
        a = A()
        self.assertEqual(a.foo2(), 2)

    def testNestedFunctionNonLocalClosure1(self):
        a = A()
        self.assertEqual(a.foo3()(), 42)

    def testNestedFunctionNonLocalClosure2(self):
        a = A()
        self.assertEqual(a.foo4(2)(15), 100)
        
    def testFunctionAndMethodTypes(self):
        self.assertEqual(str(type(foo)), "<class 'function'>")
        self.assertEqual(str(type(A.foo1)), "<class 'function'>")
        a = A()
        self.assertEqual(str(type(a.foo1)), "<class 'method'>")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

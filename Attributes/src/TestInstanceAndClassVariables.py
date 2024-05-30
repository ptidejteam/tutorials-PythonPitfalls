import unittest
from Inheritance import A, B


class Test(unittest.TestCase):

    def testClassVariablesAccess(self):
        self.assertEqual(A.cls_var1, 1)
        self.assertEqual(A.cls_var2, 2)
        
        self.assertEqual(B.cls_var1, 1)
        self.assertEqual(B.cls_var2, 3)
        self.assertEqual(B.cls_var3, 4)

    def testInstanceVariablesAccess(self):
        # Class variables
        a = A()
        self.assertEqual(a.cls_var1, 1)
        self.assertEqual(a.cls_var2, 2)
        
        b = B()
        self.assertEqual(B.cls_var1, 1)
        self.assertEqual(B.cls_var2, 3)
        self.assertEqual(B.cls_var3, 4)

        # Instance variables
        self.assertEqual(a.ins_var1, "a")
        self.assertEqual(a.ins_var2, "b")

        self.assertEqual(b.ins_var2, "c")
        self.assertEqual(b.ins_var3, "d")

    def testInstanceVariablesDynamicCreation(self):
        a1 = A()
        a1.ins_varNew1 = "w"
        self.assertEqual(a1.ins_var1, "a")
        self.assertEqual(a1.ins_var2, "b")
        self.assertEqual(a1.ins_varNew1, "w")

        a2 = A()
        a2.ins_varNew2 = "x"
        self.assertEqual(a2.ins_var1, "a")
        self.assertEqual(a2.ins_var2, "b")
        self.assertEqual(a2.ins_varNew2, "x")
        self.assertFalse(hasattr(a2, 'ins_varNew1'))
        
        b = B()
        self.assertFalse(hasattr(b, 'ins_varNew1'))
        self.assertFalse(hasattr(b, 'ins_varNew2'))
        
    def testClassVariablesDynamicCreation(self):
        A.cls_varNew1 = "y"
        self.assertTrue(hasattr(A, 'cls_varNew1'))
        self.assertTrue(hasattr(B, 'cls_varNew1'))
        b = B()
        self.assertTrue(hasattr(b, 'cls_varNew1'))
        A.cls_varNew2 = "z"
        self.assertTrue(hasattr(b, 'cls_varNew2'))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

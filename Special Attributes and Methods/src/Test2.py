import unittest
from inspect import isclass, isbuiltin
import sys


class Test(unittest.TestCase):

    def testAllBuiltIns(self):
        self.assertEqual(len(__builtins__), 158)
        pass

    def testBuiltInFunction(self):
        numberOfBuiltinFunctions = 0
        for bi in __builtins__.values():
            if isbuiltin(bi):  # Actually, "built-in functions"
                numberOfBuiltinFunctions += 1
        self.assertEqual(numberOfBuiltinFunctions, 44)

    def testBuiltInClasses(self):
        numberOfBuiltinClasses = 0
        for bi in __builtins__.values():
            if isclass(bi):
                numberOfBuiltinClasses += 1
        self.assertEqual(numberOfBuiltinClasses, 97)

    def testBuiltICallables(self):
        numberOfCallables = 0
        for bi in __builtins__.values():
            if callable(bi):
                numberOfCallables += 1
        self.assertEqual(numberOfCallables, 148)

    def testBuiltIOthers(self):
        numberOfOthers = 0
        for bi in __builtins__.values():
            if not isbuiltin(bi) and not isclass(bi):
                numberOfOthers += 1
        self.assertEqual(numberOfOthers, 17)

    def testBuiltIBooleans(self):
        numberOfBooleans = 0
        booleans = []
        for bi in __builtins__.values():
            if isinstance(bi, bool):
                booleans.append(bi)
                numberOfBooleans += 1
        self.assertEqual(numberOfBooleans, 3)  # False = False, True = True, __debug__ = True
        self.assertEqual(booleans[0], False)
        self.assertEqual(booleans[1], True)
        self.assertEqual(booleans[2], True)

    def testBuiltIBooleans2(self):
        print()
        for bi in __builtins__:
            if isinstance(__builtins__[bi], bool):
                print("Name %s, value %s" % (bi, __builtins__[bi]))
                __builtins__[bi] = True
                print("Name %s, value %s" % (bi, __builtins__[bi]))
        numberOfBooleans = 0
        booleans = []
        for bi in __builtins__.values():
            if isinstance(bi, bool):
                booleans.append(bi)
                numberOfBooleans += 1
        self.assertEqual(numberOfBooleans, 3)
        self.assertEqual(booleans[0], True)
        self.assertEqual(booleans[1], True)
        self.assertEqual(booleans[2], True)
        self.assertEqual("Hello" == "Hello", True)
        self.assertEqual("Hello" == "World", False)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

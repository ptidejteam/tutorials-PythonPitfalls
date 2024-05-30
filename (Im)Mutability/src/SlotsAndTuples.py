import unittest


class Immutable1():
    __slots__ = []
    pass


class Immutable2():
    __slots__ = ['inst_var1']
    pass


class ImmutableClassMetaClass1(type):

    def __new__(cls, name, bases, attrs):
        cls = type.__new__(cls, name, bases, attrs)
        return cls


class ImmutableWithMC1(metaclass=ImmutableClassMetaClass1):
    # __slots__ = []
    pass


class ImmutableClassMetaClass2(type):

    def __new__(cls, name, bases, attrs):
        cls = type.__new__(cls, name, bases, attrs)
        return cls


class ImmutableWithMC2(metaclass=ImmutableClassMetaClass2):
    __slots__ = []
    pass


class ImmutableClassMetaClass3(type):

    def __new__(cls, name, bases, attrs):
        attrs['__slots__'] = {}
        cls = type.__new__(cls, name, bases, attrs)
        return cls


class ImmutableWithMC3(metaclass=ImmutableClassMetaClass3):
    pass


class Test(unittest.TestCase):

    def testImmutable1(self):
        a = Immutable1()
        try:
            a.inst_var = 42
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)

    def testImmutable2(self):
        a = Immutable2()
        a.inst_var1 = 42
        self.assertEqual(a.inst_var1, 42)
        try:
            a.inst_var2 = 42
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)

    def testImmutableWithMC1(self):
        self.assertTrue('__dict__' in dir(ImmutableWithMC1))
        ImmutableWithMC1.cls_var = 42
        self.assertEqual(ImmutableWithMC1.cls_var, 42)
        self.assertTrue('__dict__' in dir(ImmutableWithMC1))

        a = ImmutableWithMC1()
        a.inst_var3 = 42
        self.assertTrue(True)

    def testImmutableWithMC2(self):
        self.assertFalse('__dict__' in dir(ImmutableWithMC2))
        ImmutableWithMC2.cls_var = 42
        self.assertEqual(ImmutableWithMC2.cls_var, 42)
        self.assertFalse('__dict__' in dir(ImmutableWithMC2))

        a = ImmutableWithMC2()
        try:
            a.inst_var3 = 42
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)

    def testImmutableWithMC3(self):
        self.assertFalse('__dict__' in dir(ImmutableWithMC3))
        ImmutableWithMC3.cls_var = 42
        self.assertEqual(ImmutableWithMC3.cls_var, 42)
        self.assertFalse('__dict__' in dir(ImmutableWithMC3))

        a = ImmutableWithMC3()
        try:
            a.inst_var3 = 42
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

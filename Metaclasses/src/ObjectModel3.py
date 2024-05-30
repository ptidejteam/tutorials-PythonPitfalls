# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example shows that Python doesn't really distinguish between class and instance methods. MC1.foo() is a class method for MC2. MC2.foo() is a class method for C1. However, it also shadows MC1.foo(), which cannot be called in MC2 any longer although MC2.foo() is an instance method of MC2 (i.e., not a class method). To overcome the shadowing, we can use the function type() that returns the class of an object (or the metaclass of a class or the meta-metaclass of a metaclass, etc.) 

class MC1(type):
    def foo(self):
        print("MC1.foo()")

    def bar(self):
        print("MC1.bar()")

class MC2(type, metaclass=MC1):
    def foo(self): 
        type(type(self)).foo(self)
        print("MC2.foo()")
    
    def xul(self):
        self.foo()
        # MC2.foo()  # TypeError: MC2.foo() missing 1 required positional argument: 'self'   
        # self.bar() # AttributeError: type object 'C1' has no attribute 'bar'
        MC2.bar()

class C1(metaclass=MC2):
    pass

print()
C1.foo()

# print()
# C1.bar() # AttributeError: type object 'C1' has no attribute 'bar'

print()
C1.xul()

# print()
# C1().foo() # AttributeError: 'C1' object has no attribute 'foo'

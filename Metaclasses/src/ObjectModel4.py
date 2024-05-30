# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example continues on combining inheritance and instantiation to show the overlapping between the two in Python. In B.foo(), super().foo() is used to access the foo() method of the object's class' superclass, A, hence A.foo(). In B.foo(), type(type(self)).foo(type(self)) is used to access the foo() method of the object's class' metaclass, MC2, hence MC2.foo().

class MC1(type):
    def foo(self):
        print("MC1.foo()")

class MC2(type, metaclass=MC1):
    def foo(self): 
        type(type(self)).foo(type(self))
        print("MC2.foo()")
    
class A():
    def foo(self):
        print("A.foo()")

class B(A, metaclass=MC2):
    def foo(self):
        super().foo()
        print("B.foo()")
        type(type(self)).foo(type(self))

# B.foo() # TypeError: A.foo() missing 1 required positional argument: 'self'
B().foo()

# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example illustrates the use of inheritance (of classes) with instantiation (of metaclasses). It is an "ideal" example because, in F.bar(), both the methods A.foo() and MC.foo() are accessible. However, if F.bar() was renamed F.foo(), then MC.foo() becomes inaccessible, only A.foo() remains accessible through super().

class MC(type):
    def foo(self):
        print("MC.foo(self)")

class A:
    def foo(self, a):
        print("A.foo(self, a)")

    # def foo(self, a, b):
    #    print("A.foo(self, a, b)")

class B:
    def foo(self, a, b):
        print("B.foo(self, a, b)")



class C(A, B):
    def bar(self):
        super().foo(0)
        # super().foo(1, 2)
        
class D(B, A):
    def bar(self):
        print("D(B, A).bar(self)")
        # super().foo(0)
        super().foo(1, 2)

class E(metaclass=MC):
    def bar(self):
        print("E(metaclass=MC).bar(self)")
        # super().foo()
        # super().foo(0)
        # super().foo(1, 2)
        E.foo()

class F(A, metaclass=MC):
    def bar(self):
        print("F(A, metaclass=MC).bar(self)")
        # super().foo()
        super().foo(0)
        # super().foo(1, 2)
        # F.foo()
        F.foo(self, 0)
        type(self).foo(self, 0)
        type(type(self)).foo(self)



c = C()
c.bar()

d = D()
d.bar()

e = E()
e.bar()

f = F()
f.bar()

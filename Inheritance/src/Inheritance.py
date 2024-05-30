# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example show the use of multiple inheritance and the need to systematically call super().<method>() to ensure proper propagation. One missing call may break the propagation, even if it is not directly in the expected chain of calls because the chain of calls is based on Python Method Resolution Order, itself based on the C3 linearisation algorithm. For example, commenting out the lines super().__init__() and super().output() in class B prevents the propagation of these calls to D and A!

# With the lines super().__init__() and super().output() in class B:
#    E
#    C
#    B
#    D
#    A
#    E.output()
#    C.output()
#    B.output()
#    D.output()
#    A.output()

# Without the lines super().__init__() and super().output() in class B:
#    E
#    C
#    B
#    E.output()
#    C.output()
#    B.output()

# The Method Resolution Order (MRO) is the set of rules that construct the linearisation. In the Python literature, the idiom "the MRO of C" is also used as a synonymous for the linearization of the class C. [https://www.python.org/download/releases/2.3/mro/]

class A:
    def __init__(self):
        print("A")
        super().__init__()
    
    def output(self):
        print("A.output()")

class B(A):
    def __init__(self):
        print("B")
        super().__init__() # Try running this code with and without this line!

    def output(self):
        print("B.output()")
        super().output() # Try running this code with and without this line!

class C(B):
    def __init__(self):
        print("C")
        super().__init__()

    def output(self):
        print("C.output()")
        super().output()

class D(A):
    def __init__(self):
        print("D")
        super().__init__()

    def output(self):
        print("D.output()")
        super().output()

class E(C, D):
    def __init__(self):
        print("E")
        super().__init__()

    def output(self):
        print("E.output()")
        super().output()

print("Single, direct inheritance")
d = C()
d.output()

print()

print("Diamond inheritance")
e = E()
e.output()

print()
print(E.mro())
print(D.mro())
print(C.mro())
print(B.mro())
print(A.mro())
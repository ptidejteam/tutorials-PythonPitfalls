# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example shows how class variables can be "shadowed" by instance variables, which, at first, take the same value as the class variables that they shadow. It also shows how easy it is to believe that the code uses one variable when it is actually using another.

class SomeMetaClass(type):
    mc_var1 = "mc_var1" # Class variable of the metaclass

    def __init__(self, name, bases, namespace):
        super().__init__(name, bases, namespace)
        self.mc_var2 = "mc_var2" # Instance variable of the metaclass

    @classmethod
    def set_mc_var1(cls, s):
        cls.mc_var1 = s
    
    def set_mc_var2(self, s):
        self.mc_var2 = s

class A(object,metaclass=SomeMetaClass):
    a_var1 = "a_var1"
    pass

class B(object,metaclass=SomeMetaClass):
    pass

class C(A):
    pass



print("+----------------------------------------+")
print("| Metaclass class and instance variables |")
print("+----------------------------------------+")

print(f"A.__class__.mc_var1 = {A.__class__.mc_var1} (id = {id(A.__class__.mc_var1)})")
print(f"C.__class__.mc_var1 = {A.__class__.mc_var1} (id = {id(A.__class__.mc_var1)})")
print(f"A.mc_var1           = {A.mc_var1} (id = {id(A.mc_var1)})")
print(f"B.mc_var1           = {B.mc_var1} (id = {id(B.mc_var1)})")
print(f"A.mc_var2           = {A.mc_var2} (id = {id(A.mc_var2)})")
print(f"B.mc_var2           = {B.mc_var2} (id = {id(B.mc_var2)})")

print()
print("A.__class__.mc_var1 = \"New value for mc_var1\"")
A.__class__.mc_var1 = "New value for mc_var1" # A.set_mc_var1("New value for mc_var1")
print(f"A.__class__.mc_var1 = {A.__class__.mc_var1} (id = {id(A.__class__.mc_var1)})")
print(f"C.__class__.mc_var1 = {A.__class__.mc_var1} (id = {id(A.__class__.mc_var1)})")
print(f"A.mc_var1           = {A.mc_var1} (id = {id(A.mc_var1)})")
print(f"B.mc_var1           = {B.mc_var1} (id = {id(B.mc_var1)})")

print()
print("A.mc_var1 = \"Another value for mc_var1\"")
A.mc_var1 = "Another value for mc_var1"
print(f"A.__class__.mc_var1 = {A.__class__.mc_var1}     (id = {id(A.__class__.mc_var1)})")
print(f"C.__class__.mc_var1 = {A.__class__.mc_var1}     (id = {id(A.__class__.mc_var1)})")
print(f"A.mc_var1           = {A.mc_var1} (id = {id(A.mc_var1)})")
print(f"B.mc_var1           = {B.mc_var1}     (id = {id(B.mc_var1)})")

print()
print("A.mc_var2 = \"New value for mc_var2\"")
A.mc_var2 = "New value for mc_var2" # A.set_mc_var2("New value for mc_var2")
print(f"A.mc_var2 = {A.mc_var2} (id = {id(A.mc_var2)})")
print(f"B.mc_var2 = {B.mc_var2}               (id = {id(B.mc_var2)})")
C.mc_var2 = "Cool value for mc_var2" # C.set_mc_var2("Cool value for mc_var2")
print(f"C.mc_var2 = {C.mc_var2}               (id = {id(C.mc_var2)})")

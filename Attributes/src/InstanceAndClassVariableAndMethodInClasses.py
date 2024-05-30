# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example shows how class variables can be "shadowed" by instance variables, which, at first, take the same value as the class variables that they shadow. It also shows how easy it is to believe that the code uses one variable when it is actually using another.

class A():
    a_var1 = "a_var1" # Class variable of the class

    def __init__(self):
        self.a_var2 = "a_var2" # Instance variable of the class
        
    @classmethod
    def set_a_var1(cls, s):
        cls.a_var1 = s
        
    def set_a_var2(self, s):
        self.a_var2 = s

class B():
    b_var1 = "b_var1"

    def __init__(self):
        self.b_var2 = "b_var2"

class C(A):
    pass



print("+------------------------------------+")
print("| Class class and instance variables |")
print("+------------------------------------+")

a1 = A()
a2 = A()

print(f"A.a_var1  = {A.a_var1} (id = {id(A.a_var1)})")
print(f"C.a_var1  = {C.a_var1} (id = {id(C.a_var1)})")
print(f"a1.a_var1 = {a1.a_var1} (id = {id(a1.a_var1)})")
print(f"a2.a_var1 = {a2.a_var1} (id = {id(a2.a_var1)})")
print(f"a1.a_var2 = {a1.a_var2} (id = {id(a1.a_var2)})")
print(f"a2.a_var2 = {a2.a_var2} (id = {id(a2.a_var2)})")

print()
print("A.a_var1 = \"New value for a_var1\"")
A.a_var1 = "New value for a_var1" # A.set_a_var1("New value for a_var1")
print(f"A.a_var1  = {A.a_var1} (id = {id(A.a_var1)})")
print(f"C.a_var1  = {C.a_var1} (id = {id(C.a_var1)})")
print(f"a1.a_var1 = {a1.a_var1} (id = {id(a1.a_var1)})")
print(f"a2.a_var1 = {a2.a_var1} (id = {id(a2.a_var1)})")

print()
print("a1.a_var1 = \"Another value for a_var1\"")
a1.a_var1 = "Another value for a_var1"
print(f"A.a_var1  = {A.a_var1}     (id = {id(A.a_var1)})")
print(f"C.a_var1  = {C.a_var1}     (id = {id(C.a_var1)})")
print(f"a1.a_var1 = {a1.a_var1} (id = {id(a1.a_var1)})")
print(f"a2.a_var1 = {a2.a_var1}     (id = {id(a2.a_var1)})")

print()
print("a1.a_var2 = \"New value for a_var2\"")
a1.a_var2 = "New value for a_var2" # a1.set_a_var2("New value for a_var2")
print(f"a1.a_var2 = {a1.a_var2} (id = {id(a1.a_var2)})")
print(f"a2.a_var2 = {a2.a_var2}               (id = {id(a2.a_var2)})")

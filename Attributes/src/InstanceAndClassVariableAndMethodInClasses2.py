# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example ilustrates how instance variables can shadow class variables and take, initially, the same values as the corresponding class variables.

class A:
    pass

a = A()

print()
print("A.attr = \"1\"")
A.attr = "1"
print(f"A.attr = {A.attr} (id = {id(A.attr)})")
print(f"a.attr = {a.attr} (id = {id(a.attr)})")

print()
print("a.attr = \"2\"")
a.attr = "2"
print(f"A.attr = {A.attr} (id = {id(A.attr)})")
print(f"a.attr = {a.attr} (id = {id(a.attr)})")

print()
print("a.attr = \"2\"")
A.attr = "3"
a.attr = "3"
print(f"A.attr = {A.attr} (id = {id(A.attr)})")
print(f"a.attr = {a.attr} (id = {id(a.attr)})")



class B:
    pass

b = B()

print()
print("b.attr = \"1\"")
b.attr = "1"
print(f"b.attr = {b.attr} (id = {id(b.attr)})")
try:
    print(f"B.attr = {B.attr} (id = {id(B.attr)})")
except:
    print("AttributeError: type object 'B' has no attribute 'attr'")

print()
print("b.attr = \"1\"")
B.attr = "2"
print(f"b.attr = {b.attr} (id = {id(b.attr)})")
print(f"B.attr = {B.attr} (id = {id(B.attr)})")

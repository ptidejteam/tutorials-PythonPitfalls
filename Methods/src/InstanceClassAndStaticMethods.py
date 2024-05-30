# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example illustrates that Python does not really have the concepts of instance, class, and static methods. All methods are "instance methods". The decorators @classmethod and @staticmethod are about the binding of the corresponding methods, not the receiver / call site and not the object model (i.e., metaclasses).

class A:
    def instanceMethod(self):
        print(f"A.instanceMethod({self})")

    @classmethod
    def classMethod(cls):
        print(f"A.classMethod({cls})")
    
    @staticmethod
    def staticMethod():
        print("A.staticMethod()")

print()
print("On A")
A.instanceMethod(A())
A.classMethod()
A.staticMethod()

print()
print("On a = A()")
a = A()
a.instanceMethod()
a.classMethod()
a.staticMethod()



class B(A):
    def instanceMethod(self):
        print(f"B.instanceMethod({self})")
    
    @classmethod
    def classMethod(cls):
        print(f"B.classMethod({cls})")
    
    @staticmethod
    def staticMethod():
        print("B.staticMethod()")

print()
print("On B")
B.instanceMethod(B())
B.instanceMethod(A())
B.classMethod()
B.staticMethod()

print()
print("On b = B()")
b = B()
b.instanceMethod()
b.classMethod()
b.staticMethod()



class C(A):
    def instanceMethod(self):
        print(f"C.instanceMethod({self})")
        try:
            super().instanceMethod()
        except:
            print("TypeError: super(type, obj): obj must be an instance or subtype of type")
         
    def classMethod(self):
        print(f"C.classMethod({self})")
        super().classMethod()
    
    def staticMethod(self):
        print("C.staticMethod()")
        super().staticMethod()

class D(C):
    pass

print()
print("On C")
C.instanceMethod(C())
C.instanceMethod(D())
C.classMethod(C())
C.staticMethod(C())

print()
print("On c = C()")
c = C()
c.instanceMethod()
c.classMethod()
c.staticMethod()

print()
print("On d = D()")
d = D()
d.instanceMethod()
d.classMethod()
d.staticMethod()

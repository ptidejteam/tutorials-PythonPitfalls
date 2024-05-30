# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

class ReferenceCountingMetaClass(type):
    def __init__(self, name, bases, namespace):
        self._instances = 0

    def __call__(self):
        newInstance = super().__call__()
        self._instances = self._instances + 1 
        return newInstance
    
    def getNumberOfInstances(self):
        return self._instances
    


class C(metaclass=ReferenceCountingMetaClass):
    pass

class D(metaclass=ReferenceCountingMetaClass):
    pass

class E():
    pass

x = C()
# print(x.getNumberOfInstances()) # getNumberOfInstances() is an instance method of the metaclass, hence a class method of the class 
print(C.getNumberOfInstances())
y = C()
print(C.getNumberOfInstances())
z = C()
print(C.getNumberOfInstances())

x = D()
# print(x.getNumberOfInstances()) # getNumberOfInstances() is an instance method of the metaclass, hence a class method of the class 
print(D.getNumberOfInstances())
y = D()
print(D.getNumberOfInstances())
z = D()
print(D.getNumberOfInstances())

x = E()
# print(x.getNumberOfInstances()) # getNumberOfInstances is not a class method of RegularClass because its metaclass is not ReferenceCountingMetaClass 
y = E()

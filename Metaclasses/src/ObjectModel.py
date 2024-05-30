# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This is a simple example illustrating the metaclass hierarchy, from the class type downwards

class MC1(type):
    pass

class MC2(type, metaclass=MC1):
    # class MC2(MC1,metaclass=MC1):    # Okay, MC1 is itself a subtype of type
    # class MC2(object,metaclass=MC1): # Error, a metaclass must (directly or indirectly) inherit from type
    pass

class C1(object, metaclass=MC2):
    pass

o1 = C1()
o2 = C1()

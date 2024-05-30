# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# Another example in which the call to super().__init__() or lack thereof produces surprising, non local, bug. With the call super().__init__() in class A, this code runs fine and prints, as expected, 2. Without the call super().__init__() in class A, the code does *not* run and the interpreter reports that: AttributeError: 'C' object has no attribute 'y'. This code behaves differently also if the base classes of C are swapped from A, B to B, A.

# https://news.ycombinator.com/item?id=24255334

class A():
    def __init__(self):
        super().__init__() # Try running this code with and without this line!
        self.x =  1

class B():
    def __init__(self):
        self.y = 2

class C(A, B): # Try swapping A and B, with and without the call to super().__init__()
    pass

print(C().y)
print(C.__mro__)

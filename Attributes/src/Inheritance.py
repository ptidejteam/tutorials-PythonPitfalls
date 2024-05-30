# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# This example shows how class variables can be "shadowed" by instance variables, which, at first, take the same value as the class variables that they shadow. It also shows how easy it is to believe that the code uses one variable when it is actually using another.


class A():
    cls_var1 = 1
    cls_var2 = 2

    def __init__(self):
        self.ins_var1 = "a"
        self.ins_var2 = "b"
        

class B(A):
    cls_var2 = 3
    cls_var3 = 4

    def __init__(self):
        self.ins_var2 = "c"
        self.ins_var3 = "d"

# Copyright Yann-Gaël Guéhéneuc, 2024
# This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License


class A():

    def __init__(self):
        super().__init__()
        self.x = 1
        self._y = 2


class B():

    def __init__(self):
        self.__z = 3


class C(A, B):
    pass


class _Z(A, B):
    pass

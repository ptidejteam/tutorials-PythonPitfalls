'''
Created on May 19, 2024

@author: Yann-Gaël Guéhéneuc
'''

import A
import net.ptidej.python.pkg1.B as B

class MyClass(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        a = A.ClassA()
        print(a)
        
        b = B.ClassB()
        print(b)
        
        print(globals())

MyClass()

class A():
    
    def foo1(self, a):
        return a
    
    def foo2(self):
        self.foo1(None)
        a = 2
        return a 

    def foo3(self, a, L=[]):
        L.append(a)


A().foo2()

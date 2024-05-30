class A(object):

    def __init__(self):
        self.ins_var = 1
        
    def foo1(self):
        print("foo1")
        a = 1

        def bar():
            print("foo1.bar")
            a = 2
            return a

        bar()
        return a

    def foo2(self):
        print("foo2")
        a = 1

        def bar():
            nonlocal a
            print("foo2.bar")
            a = 2
            return a

        bar()
        return a
    
    def foo3(self):
        print("foo3")
        a = 42

        def bar():
            nonlocal a
            print("foo2.bar")
            return a

        return bar
    
    def foo4(self, aParam):
        print("foo3")
        a = 42

        def bar(anotherParam):
            nonlocal a
            print("foo2.bar")
            return a * aParam + anotherParam + self.ins_var 

        return bar


a = 0


def foo():
    print("foo3")
    a = 1

    def bar():
        global a
        print("foo3.bar")
        a = 2

    bar()
    return a


foo()
print(a)

class A(object):

    def __init__(self):
        self.ins_var = 1

    def __enter__(self):
        print("__enter__()")
        self.ins_var += 41
        return self
        
    def __exit__(self, *args):
        print("__exit__()")
        self.ins_var = 0
    
    def foo(self):
        return self.ins_var

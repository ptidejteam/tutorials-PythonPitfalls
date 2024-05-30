if __name__ != '__main__':
    raise Exception("Only to be used as a script")



print(len("Hello, World!"))

class MyClass:
    def __len__(self):
        return 42

m = MyClass()
print(len(m))
print(m.__len__())
# print(m.len()) # AttributeError: 'MyClass' object has no attribute 'len'
# print(m.length()) AttributeError: 'MyClass' object has no attribute 'length'
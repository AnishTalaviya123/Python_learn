class A:
    def __init__(self, a):
        self.a = a
 
    def __add__(self, b):
        return self.a + b.a
ob1 = A(1)
ob2 = A(2)
print(ob1 + ob2)
class p:
    a = 4
    def __init__(self):
        print("p")

class Child1(p):
    b = 3
    def __init__(self):
        print("Child1")
        super().__init__()

class Child2(Child1):
    c = 2
    def __init__(self):
        print("Child2")
        super().__init__()

ch = Child2()
print(ch.a)
print(ch.b)
print(ch.c)

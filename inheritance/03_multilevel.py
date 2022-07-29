class p:
    a = 4

class Child1(p):
    b = 3

class Child2(Child1):
    c = 2

ch = Child2()
print(ch.a)
print(ch.b)
print(ch.c)

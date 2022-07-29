class p1:
    a = 4

class p2:
    b = 3

class p3(p1,p2):
    c = 4

ch = p3()
print(ch.a)
print(ch.b)
print(ch.c)

class employee:
    a = 10
    b = 9
    c = 8

    @classmethod
    def setattr1(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
emp = employee()
print(employee.a)
print(employee.b)
print(employee.c)
print("after change")
emp.setattr1(1, 2, 3)
print(employee.a)
print(employee.b)
print(employee.c)

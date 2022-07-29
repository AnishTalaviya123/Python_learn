class emp1:
    a = 10
    b = 9
    c = 8

    @property
    def length(self):
        return self.a
    
    @length.setter
    def length(self,value):
        self.a = value

emp =emp1()
print(emp.length)
emp.length = 20
print(emp.length)

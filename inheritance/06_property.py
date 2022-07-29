class emp1:
    a = 10
    b = 9
    c = 8

    @property
    def length(self):
        return self.a

emp =emp1()
print(emp.length)
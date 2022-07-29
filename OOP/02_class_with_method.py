class emp:
    name = "ANish"
    marks = 34
    center = "Surat"

    def printobj(self):
        print(f"My name is {self.name}")

c1 = emp()
print(c1.name)
print(c1.marks)
print(c1.center)
c1.printobj()
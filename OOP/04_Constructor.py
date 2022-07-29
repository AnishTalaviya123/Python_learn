class emp:
    center = "not known"

    def __init__(self,name,marks,center):
        self.name = name
        self.marks = marks
        self.center = center

    def printobj(self):
        print(f"The name is {self.name}")
        print(f"The marks is {self.marks}")
        print(f"The center is {self.center}")
    
    @staticmethod
    def greet():
        print("Good Day")

harry = emp("Harry", 34 , "Delhi")
rohan = emp("rohan", 84 , "Surat")
harry.printobj()
rohan.printobj()
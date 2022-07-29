class vector2d:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def printvector(self):
        print(f"{self.i}i + {self.j}j")
    
class vector3d(vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,k)
        self.k = k
    
    def printvector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")


v2 = vector2d(1, 5)
v3 = vector3d(11, 5, 9)

v2.printvector()
v3.printvector()

class Vector:
    def __init__(self,l1):
        self.data = l1
    
    def __add__(self,obj):
        myList = []
        for i in range(len(obj.data)):
            myList.append(obj.data[i] + self.data[i])
        return Vector(myList)
    
    def __len__(self):
        return len(self.data)

v1 = Vector([1,2,3])
v2 = Vector([10,12,12])
v3 = v1 + v2
print(len(v3))
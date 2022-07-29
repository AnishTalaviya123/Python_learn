mylist =[12,454,8,789,152,45]
m = 0
print(len(mylist))
for i in range(len(mylist)):
    mylist[i]  =((mylist[i]) * (mylist[i]))
    m = m + mylist[i]
print(m)
# print(mylist)
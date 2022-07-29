l1 = [1,2,3,4,5,6,7,8,9,10]

#method 1

# l2 = []
# for item in l1:
#     l2.append(item*item)
# print(l2)

#method 2
l2 = [i*i for i in l1]
print(l2)
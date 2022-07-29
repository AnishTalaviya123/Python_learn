from functools import reduce
# map
square = lambda x: x*x
l = [1,2,3,4,5]
c = map(square, l)
print(list(c))

# filter 
greater = lambda x: x>4
a = [1,2,3,4,54,67,81,8,89]
d = filter(greater, a)
print(list(d))

#reduce
sum = lambda x,y: x+y
a = [1,2,3,4]
d = reduce(sum, a)
print(d)
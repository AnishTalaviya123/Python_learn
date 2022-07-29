from functools import reduce

def max(m , n):
    if m > n :
        return m
    return n

a = [1,2,3,4,5,6,7,8,9,10]
maxNum = reduce(max, a)
print(maxNum)
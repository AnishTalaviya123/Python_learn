a = 1
b = 2 
c = 3
d = 5

if(a>b) and (a>c) and (a>d):
    ab = a
elif(b>a) and (b>c) and (b>d):
    ab = b
elif(c>a) and (c>b) and (c>d):
    ab = c
else:
    ab = d
print(ab)

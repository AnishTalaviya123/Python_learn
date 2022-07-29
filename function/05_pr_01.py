def greatest(num1,num2,num3):
    if(num1>num2):
        greatest = num1
    
    else: 
        greatest = num2
    
    if(num3 > greatest):
        greatest = num3

    return greatest
a = greatest(1,22,333)
print(a)
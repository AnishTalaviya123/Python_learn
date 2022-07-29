a = [1, 2, 3, 'Anish']

# method 1

# i = 0 
# for item in a:
#     i = i + 1
#     print(f"Item number {i} is {item}") 

#method 2
for i, item in enumerate(a):
    print(f"Item number {i+1} is {item}")
try:
    print("Hello World!")
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(a + b) # remove comment from 9 to 10 and here you have to change (a / b)
    if b > 200:
        raise Exception("This number is too large")

# except ValueError:
#     print("Value error Occurred")

except ZeroDivisionError:
    print("This is a Zero Division error")

except Exception as e:
    print(f"This problem occurred: {e}")

else:
    print("Try was Successful")

print("There were no error")

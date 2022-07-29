try:
    a = int(input("Enter a number:"))
    b = int(input("Enter another number:"))
    print(a / b)

except Exception as e:
    print(f"This problem occurred:{e}")

finally:
    print("i will always be executed")

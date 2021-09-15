# -----Try Except Exception Handling-----
a = input("Enter number 1: ")
b = input("Enter number 2: ")
try:
    print("The sum of these two numbers is", int(a) + int(b))
except Exception as e:
    print(e)
print("This line is very important")

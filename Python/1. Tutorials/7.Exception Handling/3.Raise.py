# -----Raise in Python-----
name = input("Enter your name: ").capitalize()
if name.isnumeric():
    raise Exception("Numbers are not allowed")
if name == "Harry":
    raise ValueError("Harry is blocked")
print(f"Hello {name}")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
if b == 0:
    raise ZeroDivisionError("b is 0 so stopping the program")
print(f"{a} / {b} = {a / b}")

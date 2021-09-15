# -----Faulty Calculator-----
"""
Design a calculator which will correctly solve all the problems except the followings:
45*3 = 555, 56+9 =77, 56/6 = 4
"""
print("-----CALCULATOR-----")
print("Enter operation you want to perform\n('+' for Add, '-' for Subtract, '*' for Multiply, '/' for Divide)")
op = input()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if op == "+":
    _sum = num1 + num2
    if _sum == 65:
        print("Sum is 77")
    else:
        print("Sum is", _sum)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    mul = num1 * num2
    if mul == 135:
        print("Product is 555")
    else:
        print("Product is", mul)
elif op == "/":
    if num1 == 56 and num2 == 6:
        print("Quotient is 4")
    else:
        print("Quotient is", num1 / num2)
else:
    print("Invalid Operation")

# -----Variables, Datatype and Typecasting------
var1 = "Hello "
var2 = 26
var3 = 46.5
print(type(var1), type(var2), type(var3))

var4 = "Nikhil"
print(var2 + var3)
print(var1 + var4)

var5 = "34"
var6 = "67"
print(var4 + var6)
print(var5 + var6)

# typecasting: str(), int(), float()
print(int(var5) + int(var6))
print(10 * str(int(var5) + int(var6)))
print(10 * "Hello World\n")

# In Python, value of an integer is not restricted by the number of bits and can expand to the limit of the 
# available memory.
print(100 ** 100)

# -------------Exercise--------------------
# Adding two numbers
print("Enter two numbers: ")
num1 = input()
num2 = input()
print(num1, "+", num2, "=", int(num1) + int(num2))

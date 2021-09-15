# -----Functions And Docstrings-----
a = 8
b = 9
c = sum((a, b))  # built in function
print(c)


def fun1():
    print("Hello you are in function 1")


print(fun1())


def fun2(x, y):
    average = (x + y) / 2
    print(average)


fun2(6, 5)


# Function can be copied
def func1():
    print("Nikhil Prasad")


func2 = func1
del func1
func2()


# A function can return an another function
def ret_func(num):
    if num == 0:
        return print
    if num == 1:
        return int


a = ret_func(0)
print(a)


# A function can be passed as an argument
def executor(func):
    func("Nikhil Prasad")


executor(print)


# -----Docstrings-----
def fun3(x, y):
    """This is a function which will calculate average of two numbers"""
    average = (x + y) / 2
    return average


print(fun3.__doc__)
avg = fun3(6, 5)
print(avg)

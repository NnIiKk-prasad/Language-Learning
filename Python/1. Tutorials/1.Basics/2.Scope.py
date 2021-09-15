# -----Scope, Global Variables and Global Keyword-----
a = 10  # Global variable


def fun1():
    a = 5  # Local variable
    print("Local variable:", a)


def fun2():
    global a
    a = a + 4
    print("Local variable:", a)


fun1()
fun2()
print("Global variable:", a)


def harry():
    x = 20

    def rohan():
        global x
        x = 88

    print("before calling rohan(): ", x)
    rohan()
    print("after calling rohan(): ", x)


harry()
print(x)

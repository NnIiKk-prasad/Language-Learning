# -----*args and **kwargs-----
def fun_args1(*args):
    print(type(args))
    print(args[0])


lst = ["Harry", "Rohan", "Skillf"]
fun_args1(*lst)


# normal arguments must be kept first, then *args and **kwargs
def fun_args2(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce our heroes:")
    for key, value in kwargs.items():
        print(f"{key} is our {value}")


intro = "\nThe students are:"
lst1 = ["Harry", "Rohan", "Skillf", "Hammad", "Nikhil"]
kw = {"Harry": "Monitor", "Rohan": "Instructor", "Skillf": "Coordinator",
      "Hammad": "Cook", "Nikhil": "Teacher"}
fun_args2(intro, *lst1, **kw)

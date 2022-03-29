# -----Quizzes on Functions-----

"""The type() function returns the class of the argument the object belongs to. Thus, type(int) returns which is
 of the type ‘type’ object."""
# print(type(type(int)))

""" "" depicts a null string and the join function combines the elements of the list into a string"""
# L = ['a', 'b', 'c', 'd']
# print("".join(L))

"""ord() function converts a character into its ASCII notation and chr() converts the ASCII to character"""
# print(chr(ord('A')))

"""Python explicitly defines the None object that is returned if no value is specified"""
# def add(a, b):
#     print(a + b)
#
#
# print(add(2, 3))

"""functions in python can return multiple values but as a form of tuple"""
# def func():
#     i = 34
#     j = 3.14
#     k = 3 + 4j
#     l = 'abc'
#     m = True
#     return i, j, k, l,
#
#
# print(func())

"""The function "filter" will return all items from list values which return True when passed to the function 
"checknums". "checknums" will check if the value is in the set."""
# values = [1, 2, 1, 3, 4, 2]
# numbers = set(values)
#
#
# def checknums(num):
#     if num in numbers:
#         return True
#     else:
#         return False
#
#
# for i in filter(checknums, values):
#     print(i)

"""In Python, everything is a reference, as a consequence, the function can modify the value referred by passed 
argument, i.e. the value of the variable in the caller’s scope can be changed."""
# def addToList(listcontainer):
# 	listcontainer += [10]

# mylistContainer = [10, 20, 30, 40]
# addToList(mylistContainer)
# print(len(mylistContainer))

"""The docstring can be referenced using the __doc__ attribute of the function.
And hence it prints the indexed string."""
# def gfgFunction():
# 	"Geeksforgeeks is cool website for boosting up technical skills"
# 	return 1

# print(gfgFunction.__doc__[17:21])

# -----Quizzes on Operators-----

"""unlike C/C++, in python relational operators are individually checked and returns true only if all the operations
returns true"""
# print(5 > 4 > 3)

"""Precedence of ** is higher than that of *"""
# print(3 * 1 ** 3)

"""~x is equivalent to -(x+1)"""
# print(~~~~~~5)

"""In Python, AND operator has higher precedence than OR operator. So, it is evaluated first. i.e, (b and c) evaluates
 to false. Now OR operator is evaluated"""
# a = True
# b = False
# c = False
#
# if a or b and c:
#     print("GEEKSFORGEEKS")
# else:
#     print("geeksforgeeks")

"""In Python the precedence order is first NOT then AND and in last OR"""
# a = True
# b = False
# c = False

# if not a or b:
#     print(1)
# elif not a or not b and c:
#     print(2)
# elif not a or b or not b and a:
#     print(3)
# else:
#     print(4)

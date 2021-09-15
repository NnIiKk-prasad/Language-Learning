# -----Quizzes on Data Types-----

"""strings are immutable in Python"""
# s = "Welcome"
# s[1] = 'r'

"""[::] depicts extended slicing in Python and [::-1] returns the reverse of the string"""
# print("Hello World"[::-1])

"""Partition the string into three parts using the given separator
If the separator is not found, returns a 3-tuple containing the original string and two empty strings"""
# print('cd'.partition('cd'))
# print('abef'.partition('cd'))

"""When assigning check1 to check2, we create a second reference to the same list. Changes to check2 affects 
check1. When assigning the slice of all elements in check1 to check3, we are creating a full copy of check1 
which can be modified independently (i.e, any change in check3 will not affect check1)."""
# check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
# check2 = check1
# check3 = check1[:]

# check2[0] = 'Code'
# check3[1] = 'Mcq'

# count = 0
# for c in (check1, check2, check3):
#     if c[0] == 'Code':
#         count += 1
#     if c[1] == 'Mcq':
#         count += 10

# print(count)

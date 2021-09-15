# -----Quizzes on Control Flow-----

"""if condition is false, a blank tuple will print"""
# print(tuple[1:3] if tuple == ('abcd', 786, 2.23, 'john', 70.2) else tuple())

"""enumerate() will return a tuple, the loop will have x = (0, 0), (1, 1). Thus D[0] = 0, D[1] = 1, D[0 + 7] = D[7] = 
0 and D[1 + 7] = D[8] = 1. Note: Dictionary is unordered, so the sequence of the key-value pair may differ in each 
output"""
# D = dict()
# for x in enumerate(range(2)):
#     D[x[0]] = x[1]
#     D[x[1]+7] = x[0]
# print(D)

"""The else part is not executed if control breaks out of the loop"""
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)

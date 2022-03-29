# -----Pattern printing-----
print("----Pattern Printing----")
try:
    n = int(input("Enter no. of rows you want to print: "))
    boolean = bool(int(input("Enter '0' for descending and '1' for ascending order: ")))
except ValueError:
    print("Invalid Input")
    exit()

"""1st approach"""
# if boolean:
#     i = 1
#     while i <= n:
#         j = 1
#         while j <= i:
#             print("*", end=" ")
#             j += 1
#         print()
#         i += 1
# else:
#     i = n
#     while i >= 1:
#         j = 1
#         while j <= i:
#             print("*", end=" ")
#             j += 1
#         print()
#         i -= 1

"""2nd approach"""
# if boolean:
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print("*", end=" ")
#         print()
# else:
#     for i in range(n, 0, -1):
#         for j in range(1, i + 1):
#             print("*", end=" ")
#         print()

"""3rd approach"""
# if boolean:
#     for i in range(1, n + 1):
#         for n in range(i):
#             print("*", end=" ")
#         print()
# else:
#     for i in range(n, 0, -1):
#         for n in range(i):
#             print("*", end=" ")
#         print()

"""4th approach"""
if boolean:
    for i in range(1, n + 1):
        print("*" * i)
else:
    for i in range(n, 0, -1):
        print("*" * i)

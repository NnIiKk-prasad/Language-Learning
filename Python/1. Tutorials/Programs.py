# -----Basic Python Programs-----
"""Swapping two numbers"""
# a = 5
# b = 9
# a, b = b, a
# print(a, b)

"""Check prime number"""
# n = int(input("Enter a number: "))
# if n < 2:
#     print("Not a prime number")
# else:
#     for i in range(2, n // 2):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")

"""Check leap year"""
# year = int(input("Enter an year: "))
# result = "Leap Year" if year % 400 == 0 else "Leap Year" if year % 4 == 0 and year % 100 != 0 else "Non Leap Year"
# print(result)

"""Print first N odd natural numbers in reverse order"""
# n = int(input("Enter a number: "))
# for i in range(n):
#     print(2 * n + 1 - 2 * i, end=" ")

# for i in range(2 * n + 1, 0, -2):
#     print(i, end=" ")

"""Remove duplicate characters from a string"""
# s = input("Enter a string: ")
# i = 0
# s1 = ""
# for x in s:
#     if s.index(x) == i:
#         s1 += x
#     i += 1
# print(s1)

"""Sort a list of numbers"""
# l = [int(x) for x in input("Enter numbers separated by comma:\n").split(',')]
# print(sorted(l))    # it doesn't sort 'l' but returns sorted of 'l'
# l.sort()    # it will sort 'l'
# print(l)

"""Print index of all occurrence of given element in a given list"""
# l = [eval(x) for x in input("Enter numbers separated by comma:\n").split(',')]
# element = int(input("Enter a number from above: "))
# index = 0
# for item in l:
#     if item == element:
#         print(index, end=" ")
#     index += 1

"""Remove duplicate from a list of strings"""
# lst = [item.strip() for item in input("Enter some items separated by comma:\n").split(',')]
# [item for item in set(lst) if print(item, end=" ")]

"""Arrange words in dictionary order"""
# print([x for x in sorted(input("Enter comma separated words:\n").split(','))])
# [x for x in sorted(input("Enter comma separated words:\n").split(',')) if print(x, end=" ")]

"""Greatest number in a tuple"""
# t = tuple([int(x) for x in input("Enter numbers separated by comma:\n").split(',')])
# print(f"Greatest number in the tuple is {max(t)}")

"""Reverse a tuple"""
# lst = [int(x) for x in input("Enter numbers separated by comma:\n").split(',')]
# lst.reverse()
# print(tuple(lst))

"""Compare Two Tuples"""
# t1 = tuple([int(x) for x in input("Enter numbers separated by comma for first tuple:\n").split(',')])
# t2 = tuple([int(x) for x in input("Enter numbers separated by comma for second tuple:\n").split(',')])
# if t1 == t2:
#     print("Yes, tuples are same")
# else:
#     print("No, tuples are not same")

"""Merge two tuples"""
# t1 = tuple(sorted([int(x) for x in input("Enter numbers separated by comma for first tuple:\n").split(',')]))
# t2 = tuple(sorted([int(x) for x in input("Enter numbers separated by comma for second tuple:\n").split(',')]))
# t3 = []
# i, j = 0, 0
# while i < len(t1) and j < len(t2):
#     if t1[i] < t2[j]:
#         t3.append(t1[i])
#         i += 1
#     else:
#         t3.append(t2[j])
#         j += 1
# if i == len(t1):
#     while j < len(t2):
#         t3.append(t2[j])
#         j += 1
# else:
#     while i < len(t1):
#         t3.append(t1[i])
#         i += 1
# print(f"Resulting tuple is: {tuple(t3)}")

"""Create Homogeneous Tuples form Heterogeneous Tuple"""
# x = (30, 4.5, 26, 3 + 4j, 'abc', True, 5.6, 2 - 1j)
# t1, t2, t3, t4, t5 = [], [], [], [], []
# for e in x:
#     if type(e) == int:
#         t1.append(e)
#     elif type(e) == float:
#         t2.append(e)
#     elif type(e) == complex:
#         t3.append(e)
#     elif type(e) == str:
#         t4.append(e)
#     elif type(e) == bool:
#         t5.append(e)
# print(tuple(t1), tuple(t2), tuple(t3), tuple(t4), tuple(t5), sep="\n")

"""Count Frequency of Elements of a Tuple"""
# t1 = tuple([int(x) for x in input("Enter numbers separated by comma:\n").split(',')])
# i = 0
# for e in t1:
#     if i == t1.index(e):
#         print(f"{e} - {t1.count(e)}")
#     i += 1

"""Print list of first N prime numbers"""


# def nextPrime(num):
#     while True:
#         num += 1
#         for i in range(2, num // 2):
#             if num % i == 0:
#                 break
#         else:
#             return num
#
#
# def primeProducer(n):
#     num, count = 1, 1
#     while count <= n:
#         num = nextPrime(num)
#         yield num
#         count += 1
#
#
# lst = [x for x in primeProducer(20)]
# print(lst)

"""Single line function to calculate factorial"""
# factorial = lambda x: x * factorial(x - 1) if x > 0 else 1
# print(factorial(int(input("Enter a number: "))))

"""Recursive Python function to print first N even natural numbers"""
# def printNeven(n):
#     if n > 0:
#         printNeven(n - 1)
#         print(2 * n, end=" ")
#
#
# n = int(input("Enter a number: "))
# print(f"First {n} even natural numbers are:")
# printNeven(n)

"""Recursive function to calculate sum of first N natural numbers"""
# def firstNsum(n):
#     if n == 1:
#         return 1
#     return n + firstNsum(n - 1)
#
#
# n = int(input("Enter a number: "))
# print(f"Sum of first {n} natural numbers is: {firstNsum(n)}")

"""Recursive function to calculate sum of squares of first N natural numbers"""
# def firstNsquareSum(n):
#     if n == 1:
#         return 1
#     return n ** 2 + firstNsquareSum(n - 1)
#
#
# n = int(input("Enter a number: "))
# print(f"Sum of square first {n} natural numbers is: {firstNsquareSum(n)}")

"""Add two matrices"""
# def matrix(m, n):
#     M = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             val = int(input(f"Enter M[{i + 1}][{j + 1}]: "))
#             row.append(val)
#         M.append(row)
#     return M

# def matricesSum(A, B):
#     Output = []
#     for i in range(len(A)):
#         row = []
#         for j in range(len(A[0])):
#             row.append(A[i][j] + B[i][j])
#         Output.append(row)
#     return Output

# m = int(input("Enter the value of m: "))
# n = int(input("Enter the value of n: "))

# A = matrix(m, n)
# print(f"Matrix A: {A}")

# B = matrix(m, n)
# print(f"Matrix B: {B}")

# S = matricesSum(A, B)
# print(f"Matrix sum of A and B is: {S}")

"""Multiply two matrices"""
# def matrix(m, n):
#     M = []
#     for i in range(m):
#         row = []
#         for j in range(n):
#             val = int(input(f"Enter M[{i + 1}][{j + 1}]: "))
#             row.append(val)
#         M.append(row)
#     return M

# def matricesProduct(A, B):
#     Output = []
#     for i in range(len(A)):
#         row = []
#         for j in range(len(B[0])):
#             val = 0
#             for k in range(len(A[0])):
#                 val = val + A[i][k] * B[k][j]
#             row.append(val)
#         Output.append(row)
#     return Output

# m = int(input("Enter no. of rows of 1st matrix: "))
# n = int(input("Enter no. of columns of 1st matrix: "))
# A = matrix(m, n)
# print(f"Matrix A: {A}")

# m = int(input("Enter no. of rows of 2nd matrix: "))
# if m != n:
#     print("No. of rows of 2nd matrix must be equal to no. of columns of 1st matrix")
#     exit()
# n = int(input("Enter no. of columns of 2nd matrix: "))
# B = matrix(m, n)
# print(f"Matrix B: {B}")

# P = matricesProduct(A, B)
# print(f"Matrix product of A & B is: {P}")

"""Check Armstrong number"""
# def isArmstrong(n):
#     order = len(str(n))
#     temp = n
#     sum = 0
#     while n:
#         digit = n % 10
#         sum += digit ** order
#         n //= 10
#     if sum == temp:
#         return True
#     return False

# num = int(input("Enter a number: "))
# if isArmstrong(num):
#     print("Yes")
# else:
#     print("No")

"""LCM of two numbers"""
# def LCM(num1, num2):
#     temp = max(num1, num2)
#     while True:
#         if temp % num1 == 0 and temp % num2 == 0:
#             break
#         temp += 1
#     return temp

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print(f"LCM of {num1} and {num2} is {LCM(num1, num2)}")

"""HCF/GCD of two numbers"""
# def HCF(num1, num2):
#     temp = min(num1, num2)
#     while True:
#         if num1 % temp == 0 and num2 % temp == 0:
#             break
#         temp -= 1
#     return temp

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print(f"HCF of {num1} and {num2} is {HCF(num1, num2)}")

"""nth fibonacci number"""
# def fiboItter(n):
#     if n == 0 or n == 1:
#         return n
#     preprevious = 0
#     previous = 1
#     for i in range(n - 1):
#         sum = preprevious + previous
#         preprevious = previous
#         previous = sum
#     return sum

# def fiboRecur(n):
#     if n == 0 or n == 1:
#         return n
#     return fiboRecur(n - 1) + fiboRecur(n - 2)

# n = int(input("Enter a number: "))
# print(f"Fibonacci number at {n} is {fiboRecur(n)}")
# print(f"Fibonacci number at {n} is {fiboItter(n)}")

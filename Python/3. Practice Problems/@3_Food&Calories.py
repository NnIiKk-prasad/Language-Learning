# Practice Problem 3 - Foods and Calories
import re

str = input("Enter list of calories: ")
lst = re.findall(r"\d+", str)
for index, item in enumerate(lst):
    lst.pop(index)
    lst.insert(index, int(item))
lst.sort()
print(f"\nEntered list of calories: {lst}")

lst1 = lst.copy()
lst1.reverse()
print(f"\nInbuilt method to reverse the list: {lst1}")

lst2 = lst.copy()
print(f"\nlist slicing method to reverse the list: {lst2[::-1]}")

lst3 = lst.copy()
for i in range(len(lst3) // 2):
    lst3[i], lst3[len(lst3) - i - 1] = lst3[len(lst3) - i - 1], lst3[i]
print(f"\nSwapping method to reverse the list: {lst3}")

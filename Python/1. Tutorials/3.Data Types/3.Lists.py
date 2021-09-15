# -----Lists And List Methods-----
grocery = ["Harpic", "Vim bar", "Toothpaste", "Bhindi", 56]
print(grocery[4])
print(grocery)

numbers = [2, 9, 7, 11, 3]
print(numbers[1:4])
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

num1 = []  # empty list
num1.append(2)
num1.append(45)
print(num1)
num1.insert(1, 34)
num1.insert(1, 8)
print(num1)
num1.remove(34)
num1.pop()
print(num1)
num1[0] = 1
print(num1)

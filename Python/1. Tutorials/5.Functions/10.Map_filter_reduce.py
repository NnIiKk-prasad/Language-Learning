# -----Map, Filter & Reduce-----
# reduce function
from functools import reduce

list1 = [1, 2, 3, 4, 5]
prod = reduce(lambda x, y: x * y, list1)
print(prod)

# map function
num = ["3", "34", "64"]
# for i in range(len(num)):
#     num[i] = int(num[i])
num = list(map(int, num))
num[2] = num[2] + 1
print(num)
print(map(int, num))

num1 = [6, 4, 8, 21, 3]
square = list(map(lambda x: x * x, num1))
print(square)

func = [lambda x: x * x, lambda x: x * x * x]
for i in range(5):
    print(list(map(lambda x: x(i), func)))


# filter function
def is_greater_5(x):
    return x > 5


print(list(filter(is_greater_5, num1)))

# -----Anonymous or Lambda Functions-----
add = lambda a, b: a + b
print(add(5, 7))

a = [[8, 23], [5, 6], [1, 14]]
a.sort(key=lambda x: x[1])
print(a)

# -----Tuple and it's methods-----
tp = ()  # Empty tuple
print(type(tp))
print(tp)

# t1 = (1) # Wrong way to declare a Tuple with Single element
t1 = (1,)  # Tuple with Single element
print(t1)

# Tuple is immutable(cannot be changed)
# tp[1] = 45 # throws an error

# Creating a tuple using ()
t = (1, 2, 4, 5)

# Printing the elements of a tuple
print(t[0])

# Tuple methods
t = (1, 2, 4, 5, 4, 1, 2, 1, 1)

print(t.count(1))
print(t.index(5))

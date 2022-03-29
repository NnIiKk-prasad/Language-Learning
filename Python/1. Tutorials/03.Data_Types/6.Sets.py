# -----Sets & It's Methods-----
s = set()  # Empty set
print(type(s))

s.add(1)
s.add(1)  # Adding a value repeatedly does not changes a set
s.add(2)
s.add(4)
s.add(5)
s.add((4, 5, 6))
print(s)

# s.add({4:5}) # Cannot add list or dictionary to sets

print(len(s)) # Prints the length of this set

s.remove(5) # Removes 5 fromt set b
# s.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(s)

print(s.pop())
print(s)

s1 = s.union({1, 2, 3})
s2 = s.intersection({1, 2, 3})
print(s, s1, s2)

s3 = {4, 6}
print(s.isdisjoint(s3))

s_from_list = set([1, 3, 6, 4])
print(s_from_list)

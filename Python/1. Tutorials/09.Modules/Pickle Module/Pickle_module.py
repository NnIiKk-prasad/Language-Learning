# -----Pickle Module-----
"""
pickle.dump() - This function is equivalent to Pickler(file, protocol).dump(obj). This is used to write a
                pickled representation of obj to the open file object file.
pickle.dumps() - This function returns the pickled representation of the object as a bytes object.
pickle.load() - This function is equivalent to Unpickler(file).load(). This function is used to read a pickled object
                representation from the open file object file and return the reconstituted object hierarchy specified.
pickle.loads() - This function is used to read a pickled object representation from a bytes object and return the
                 reconstituted object hierarchy specified.
"""
import pickle

# Python program to illustrate pickle.dump()
# cars = ["Audi", "BMW", "Tesla"]
# file = "mycars.pkl"
# fileobj = open(file, "wb")
# pickle.dump(cars, fileobj)
# fileobj.close()

# Python program to illustrate pickle.load()
file = "mycars.pkl"
fileobj = open(file, "rb")
mycars = pickle.load(fileobj)
print(mycars)
fileobj.close()

# Python program to illustrate pickle.dumps()
data1 = [{'a': 'A', 'b': 2, 'c': 3.0}]
data1_string = pickle.dumps(data1)
print('PICKLE:', data1_string)

# Python program to illustrate pickle.loads()
print('BEFORE:', data1)
data2 = pickle.loads(data1_string)
print('AFTER:', data2)

print('SAME?:', (data1 is data2))
print('EQUAL?:', (data1 == data2))

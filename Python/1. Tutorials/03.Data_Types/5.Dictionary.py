# -----Dictionary & Its Functions-----
d1 = {}  # Empty dictionary
print(type(d1))

dict1 = {"Nikhil": "Burger", "Rohan": "Fish", "Harry": {"B": "Maggie", "L": "Chapati", "D": "Chicken"}}

print(dict1["Nikhil"])
print(dict1.get("Nikhil"))
print(dict1["Harry"]["B"])

dict1.update({"Leena": "Toffee"})
print(dict1)

dict1[420] = "Kebabs"
print(dict1)

del dict1[420]
print(dict1)

dict2 = dict1  # Here dict2 and dict1 refers to same memory address
del dict2["Harry"]
print(dict1)

dict3 = dict1.copy()  # Here dict3 is a copy of dict1
del dict3["Rohan"]
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())

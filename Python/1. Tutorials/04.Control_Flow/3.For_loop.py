# -----For loops-----
list1 = ["Harry", "Larry", "Carry", "Marry"]
for item in list1:
    print(item)

list2 = [["Harry", 2], ["Larry", 5], ["Carry", 8], ["Marry", 25]]
for item, number in list2:
    print(item, "has", number, "lollipops")

dict1 = dict(list2)
for item, number in dict1.items():
    print(item, "has", number, "lollipops")

items = [int, float, "Harry", 2, 5, 8, 56, 64]
for item in items:
    if str(item).isnumeric() and item > 6:
        print(item)

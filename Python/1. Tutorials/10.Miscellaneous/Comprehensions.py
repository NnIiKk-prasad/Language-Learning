# -----Comprehensions-----

# list comprehension
lst = [i for i in range(100) if i % 3 == 0]
print(lst)

# dictionary comprehension
dict1 = {i: f"Item{i}" for i in range(1, 101) if i % 10 == 0}
print(dict1)

dict2 = {value: key for key, value in dict1.items()}  # to reverse key, value of a dictionary
print(dict2)

# set comprehension
dress = {dress for dress in ["Dress1", "Dress2", "Dress4", "Dress2", "Dress1"]}
print(dress)

# generator comprehension
evens = (i for i in range(101) if i % 2 == 0)
print(type(evens))
for item in evens:
    print(item, end=" ")

# -------------Exercise--------------------
try:
    n = int(input("\nEnter number of items you want to print: "))
    print(f"Enter {n} items separated by ',':")
    items = input()
    lst1 = [item.strip().capitalize() for item in items.split(",")]
    print("In which format you want to see your items:\n"
          "Press 1 for list\n"
          "Press 2 for set\n"
          "Press 3 for dictionary\n")
    ch = input("Enter your choice: ")
    if ch == '1':
        print(lst1)
    elif ch == '2':
        set1 = {item for item in lst1}
        print(set1)
    elif ch == '3':
        dict3 = {f"Item {i + 1}": item for i, item in enumerate(lst1)}
        print(dict3)
    else:
        print("Invalid input")
except Exception as e:
    print(e)

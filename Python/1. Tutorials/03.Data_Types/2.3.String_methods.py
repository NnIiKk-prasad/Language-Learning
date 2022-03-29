# -----String Methods-----

my_str = "Nikhil is a good boy"

print(len(my_str))
print(my_str.isalnum())
print(my_str.isalpha())
print(my_str.endswith("boy"))
print(my_str.count('o'))
print(my_str.find("is"))
print(my_str.index("is"))
print(my_str.capitalize())
print(my_str.upper())
print(my_str.lower())
print(my_str.replace("is", "are"))
print(",".join(my_str))
print(my_str.split(" "))

# --------Exercise--------
letter = '''\nDear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and regards,
Bill
Date: <|DATE|>
'''
name = input("\nEnter Your Name: ")
date = input("Enter Date: ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

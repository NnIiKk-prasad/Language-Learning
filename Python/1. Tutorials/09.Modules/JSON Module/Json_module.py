# -----Json Modules-----
import json

# Parse JSON (Convert from JSON to Python)
data1 = '{"var1":"Nikhil", "var2":56}'   # JSON string
parsed = json.loads(data1)   # Convert string to Python dict
print(type(parsed))
print(parsed)

# Convert from Python to JSON
data2 = {
    "name": "Nikhil Prasad",
    "cars": ["BMW", "Ferrari", "Tesla"],
    "fridge": ("Roti", 540),
    "isbad": False
}
json_object = json.dumps(data2, indent=4)
print(type(json_object))
print(json_object)

# Writing JSON to a file
data3 = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
with open("sample.json", "w") as outfile:
    json.dump(data3, outfile)

# Python read JSON file
with open('sample.json') as f:
    data4 = json.load(f)
print(data4)

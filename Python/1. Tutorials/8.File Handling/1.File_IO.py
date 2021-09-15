# -----File IO Basics-----
"""
"r" - Open a file for reading - default
"w" - Open a file for writing
"x" - Creates fies if not exists
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write
"""
f = open("nikhil.txt")
content = f.read()
print(content)
f.close()

f = open("nikhil.txt", "rb")
content = f.read()
print(content)
f.close()

f = open("nikhil.txt", "rt")
content = f.read(4)
print("1", content)
content = f.read(4)
print("2", content)
f.close()

f = open("nikhil.txt", "rt")
for line in f:
    print(line, end="")
f.close()
print()

f = open("nikhil.txt", "rt")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("nikhil.txt", "rt")
print(f.readlines())
f.close()

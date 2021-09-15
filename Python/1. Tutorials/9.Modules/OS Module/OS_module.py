# -----Os Module-----
import os

print(dir(os))

print(os.getcwd())

os.chdir("F:\\")
print(os.getcwd())
print(os.listdir())

# The "r" in the beginning is making sure that the string is being treated as a "raw string"
os.chdir(r"C:\Users\NALIN KR\Documents\Programming Tutorials\Language Learning\Python\1. Tutorials\9.Modules\OS Module")
print(os.getcwd())

# os.mkdir("Dir")
# os.makedirs("This\\that")

# os.rename("OS.txt", "os.txt")

print(os.environ.get("Path"))

print(os.path.join("C:\\", "harry_ex.txt"))

print(os.path.exists(r"C:\Windows10Upgrade"))
print(os.path.isdir(r"C:\Program Files"))

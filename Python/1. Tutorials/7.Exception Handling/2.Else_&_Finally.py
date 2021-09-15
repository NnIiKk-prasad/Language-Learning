# -----Else & Finally In Try Except-----
f1 = open(r"C:\Users\NALIN KR\Documents\Programming Tutorials\Language Learning\Python\1. Tutorials\7.Exception Handling\nikhil.txt")

try:
    f2 = open(r"C:\Users\NALIN KR\Documents\Programming Tutorials\Language Learning\Python\1. Tutorials\7.Exception Handling\not_exist.txt")

except IOError as e:
    print("IO error occurred:", e)

except EOFError as e:
    print("EOF error occurred:", e)

else:
    print("This will run only when except is not running")
    f2.close()

finally:
    print("This will run anyway")
    f1.close()

print("This line is very important")

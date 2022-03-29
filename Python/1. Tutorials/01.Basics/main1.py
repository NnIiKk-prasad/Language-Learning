def print_str(str):
    return f"The string is: {str}"


def add(a, b):
    return a + b

# If the source file is executed as the main program, the interpreter sets the __name__ variable to "__main__".
# And if this file is being imported from another module, __name__ will be set to the module’s name.
print("And the name is", __name__)

if __name__ == '__main__':
    print(print_str("Nikhil"))
    print(add(5, 6))

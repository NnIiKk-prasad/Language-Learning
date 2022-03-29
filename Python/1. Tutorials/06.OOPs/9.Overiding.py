# -----Super() and Overriding In Classes-----
class A:
    class_var1 = "Class variable of class A."

    def __init__(self):
        print("Class A's constructor.")
        self.class_var1 = "Instance variable of class A."
        self.special = "Special"


class B(A):
    class_var1 = "Class variable of class B."   # Attribute Overriding

    def __init__(self):   # Constructor Overriding
        # super().__init__()
        print("Class B's constructor.")
        self.class_var1 = "Instance variable of class B."
        super().__init__()
        print(super().class_var1)


a = A()
b = B()

print(b.class_var1)

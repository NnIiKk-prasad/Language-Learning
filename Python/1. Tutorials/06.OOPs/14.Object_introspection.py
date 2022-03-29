# ----Object Introspection-----
import inspect


class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set. Please set it using setter."
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


nikhil = Employee("Nikhil", "Prasad")

print(type(nikhil))
print(id(nikhil))
print(dir(nikhil))
print(inspect.getmembers(nikhil))

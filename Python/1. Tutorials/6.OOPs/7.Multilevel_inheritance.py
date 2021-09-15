# -----Multilevel Inheritance-----
class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}."

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def well_done(string):
        return f"Well done! {string}"


class Programmer(Employee):
    def __init__(self, name, salary, role, languages):   # Constructor Overriding
        super().__init__(name, salary, role)
        self.languages = languages

    def print_details(self):   # Method Overriding
        return f"The programmer name is {self.name}. Salary is {self.salary}. Role is {self.role}. " \
               f"Languages known: {self.languages}"


class CoolProgrammer(Programmer):
    no_of_leaves = 12


harry = Employee("Harry", 45000, "Manager")
rahul = Programmer("Rahul", 15000, "Intern", ["C++"])
karan = CoolProgrammer("Karan", 25000, "Intern", ["C++", "Python"])

print(harry.print_details(), f"No. of leaves: {harry.no_of_leaves}")
print(rahul.print_details(), f"No. of leaves: {rahul.no_of_leaves}")
print(karan.print_details(), f"No. of leaves: {karan.no_of_leaves}")

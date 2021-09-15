# -----Class, Instance & Class Variables-----
class Student:
    pass


# garry and larry are two instances of class Student
garry = Student()
larry = Student()
print(garry, larry)

garry.name = "Garry"
garry.std = 12
larry.section = 'A'
larry.subjects = ["Hindi", "Physics", "Maths"]
print(garry.name, garry.std, larry.section, larry.subjects)


class Employee:
    no_of_leaves = 8   # Attribute


rohan = Employee()
rohan.name = "Rohan"
rohan.salary = 40000

harry = Employee()
harry.name = "Harry"
harry.salary = 45000

print(rohan.no_of_leaves, harry.no_of_leaves, Employee.no_of_leaves)

print(rohan.__dict__)
rohan.no_of_leaves = 9  # can't change class attribute like this
print(rohan.__dict__)

print(rohan.no_of_leaves, harry.no_of_leaves, Employee.no_of_leaves)

print(Employee.__dict__)
Employee.no_of_leaves = 10  # can change class attribute like this
print(Employee.__dict__)

print(rohan.no_of_leaves, harry.no_of_leaves, Employee.no_of_leaves)

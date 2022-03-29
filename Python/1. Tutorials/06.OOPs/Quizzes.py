# -----Quizzes on OOPs-----

"""The value 555 is not retained in the object as it is not assigned to a data attribute of the class/object. 
So, the output of the program is 111"""

# class Acc:
#     def __init__(self, id):
#         self.id = id
#         id = 555
#
#
# acc = Acc(111)
# print(acc.id)

"""In this program we are creating a member variable having name 'life' by adding it directly to the dictionary
 of the object 'manager' of class 'Geeks'. Total numbers of items in the dictionary is 2, the variables 'life' and 'id'."""
# class Geeks:
# 	def __init__(self, id):
# 		self.id = id

# manager = Geeks(100)

# manager.__dict__['life'] = 49

# print (manager.life + len(manager.__dict__))

"""In Python, class variables are internally handled as dictionaries. If a variable name is not found in the 
dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the referenced 
variable name is found, if the variable is not found error is being thrown."""
# class A(object):
# 	val = 1

# class B(A):
# 	pass

# class C(A):
# 	pass

# print (A.val, B.val, C.val)
# B.val = 2
# print (A.val, B.val, C.val)
# A.val = 3
# print (A.val, B.val, C.val)

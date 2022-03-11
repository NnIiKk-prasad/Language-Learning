# -----Miscellaneous Quizzes-----

""".2 defines the precision of the floating point number"""
# print('{0:.2}'.format(1.0 / 3))

"""The % converts the number to percentage with respect to 1.0"""
# print('{0:%}'.format(6.0 / 3))
# print('{0:-5}'.format(6 / 3))

"""Neither of 0.1, 0.2 and 0.3 can be represented accurately in binary. The round off errors from 0.1 and 0.2
accumulate and hence there is a difference of 5.5511e-17 between (0.1 + 0.2) and 0.3"""
# print(0.1 + 0.2 == 0.3)

""" The third function call is the weird one. It uses the original list stored in the original memory block. 
That is why it starts off with 0 and 1."""
# def gfg(x,l=[]):
# 	for i in range(x):
# 		l.append(i*i)
# 	print(l)

# gfg(2)
# gfg(3,[3,2,1])
# gfg(3)

"""When addition(+) operator uses list as its operands then the two lists will get concatenated. And when a list 
id multiplied with a constant k>=0 then the same list is appended k times in the original list."""
# list1 = [1998, 2002, 1997, 2000]
# list2 = [2014, 2016, 1996, 2009]

# print("list1 + list2 = : ", list1 + list2)

# print("list1 * 2 = : ", list1 * 2)

"""\\x is an escape sequence that means the following 2 digits are a hexadecimal number encoding a character"""
# print('\x25\x26')

"""To sort a dictionary by value"""
# {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
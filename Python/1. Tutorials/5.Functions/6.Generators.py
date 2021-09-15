# -----Generators-----
"""
Iterable - python object which define __iter__() or __getitem__()
         - ex: list, str, tuple, set, dict, etc
Iterator - python object which points to the items in iterable object and define __next__()
Generators - functions which yields series of data on the fly according to some logical pattern
           - it returns an iterator object
           - ex: range(), etc
"""
my_list = [10, 20, 30, 40, 50, 60]  # my_list is an iterable object
it1 = iter(my_list)  # it is an iterator object of the list 'my_list'
while True:
    try:
        print(next(it1))
    except StopIteration:
        break


def evenNumbers(n):     # evenNumbers(n) is a generator because it uses yield keyword to return values
    i = 1
    while n:
        yield i * 2
        i += 1
        n -= 1


it2 = evenNumbers(10)    # it2 is an iterator object of the generator 'evenNumbers(n)'
even_list = []
while True:
    try:
        even_list.append(next(it2))
    except StopIteration:
        break

print(even_list)


# nth Fibonacci number
def nth_fib_num(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib_num(n - 1) + nth_fib_num(n - 2)


# -------------Exercise--------------------
# Fibonacci number generator
def fib(n):
    while n:
        fibonacci = nth_fib_num(n)
        yield fibonacci
        n -= 1


num = int(input("Enter a number greater than 0: "))
if num > 0:
    it3 = fib(num)
    fibonacci_list = []
    while True:
        try:
            fibonacci_list.append(next(it3))
        except StopIteration:
            break

    print(f"First {num} fibonacci numbers are:")
    print(fibonacci_list[::-1])
else:
    print("Invalid input")

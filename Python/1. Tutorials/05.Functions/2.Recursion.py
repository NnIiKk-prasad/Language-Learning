# -----Recursions-----
# Factorial using iteration
def fact_iterative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i + 1)
    return fact


# Factorial using recursion
def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recursive(n - 1)


# nth Fibonacci number
def nth_fib_num(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib_num(n - 1) + nth_fib_num(n - 2)


num = int(input("Enter a number: "))
print("Factorial using iterative method:", fact_iterative(num))
print("Factorial using recursive method:", fact_recursive(num))
print("Fibonacci number at", num, "is:", nth_fib_num(num))

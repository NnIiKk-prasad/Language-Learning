"""
Part 1 - Calculate the factorial of a given number
Part 2 - Find the number of trailing zeroes in that factorial  
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def trailingZeroes(num):
    # fact = factorial(num)
    # no_of_zeroes = 0
    # while True:
    #     if fact % 10 != 0:
    #         break
    #     no_of_zeroes += 1
    #     fact //= 10
    # return no_of_zeroes
    count = 0
    i = 5
    while num // i != 0:
        count += int(num / i)
        i = i * 5
    return count

if __name__ == "__main__":
    try:
        number = int(input("Enter a positive integer: "))
    except ValueError:
        print("Enter positive integers only.")
        exit()
    if number < 0:
        print("Enter positive integers only.")
        exit()
    
    print(f"Factorial of {number} is {factorial(number)}")
    print(f"No. of trailing zeroes is {trailingZeroes(number)}")

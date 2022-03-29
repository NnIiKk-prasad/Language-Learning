# -----Guess the number-----
print("Guess the number")
n = 18
i = 9
while i > 0:
    num = int(input("Enter your guess: "))
    i -= 1
    if num > n:
        print("Your guess is greater than the number. You have now", i, "guesses left.")
    elif num == n:
        print("Congrats! you have guessed the number in", 9 - i, "iteration")
        break
    else:
        print("Your guess is lower than the number. You have now", i, "guesses left.")
print("Game Over")

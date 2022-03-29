# Practice Problem 6 - Guess the number
import random


class Player:
    guess_count = 0

    def __init__(self, name, a, b):
        self.name = name
        self.random = random.randint(a, b)

    def number_guess(self, a, b):
        while True:
            print(f"\nPlease guess a number between {a} to {b} (including {a} and {b})")
            guess = int(input())
            if guess < a or guess > b:
                print("\nPlesae enter number within the specified limit")
                continue
            if guess == self.random:
                self.guess_count += 1
                print(
                    f"\nCorrect! You took {self.guess_count} trails to guess the number")
                break
            elif guess > self.random:
                self.guess_count += 1
                print("\nWrong guess! Please lower your guess")
            else:
                self.guess_count += 1
                print("\nWrong guess! Please higher your guess")


if __name__ == '__main__':
    print("-----Guess the number-----")
    try:
        a = int(input("Enter min value of range: "))
        b = int(input("Enter max value of range: "))
        if a > b:
            print("\n\nThis cannot be the range as minimum should be less than maximum")
            exit()
        name = input("\nPlayer 1:\nPlease enter your name: ").capitalize()
        player1 = Player(name, a, b)
        player1.number_guess(a, b)
        name = input("\nPlayer 2:\nPlease enter your name: ").capitalize()
        player2 = Player(name, a, b)
        player2.number_guess(a, b)
        if player1.guess_count < player2.guess_count:
            print(
                f"\n{player1.name} wins by {player2.guess_count - player1.guess_count} less trails")
        elif player1.guess_count > player2.guess_count:
            print(
                f"\n{player2.name} wins by {player1.guess_count - player2.guess_count} less trails")
        else:
            print(
                f"\nIts a tie. You both took {player1.guess_count} trails to guess the number")
    except ValueError:
        print("Enter Integers only")
        exit()

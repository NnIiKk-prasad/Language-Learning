# -----Stone, Paper, Scissor Game-----
import random
print("--Stone, Paper, Scissor Game--")
lst = ["Stone", "Paper", "Scissor"]
Round = 1
user_points = 0
com_points = 0
while Round <= 10:
    print(f"\nRound: {Round}  (Total: 10)")
    print("Press 1 for 'Stone', 2 for 'Paper' and 3 for 'Scissor'")
    try:
        temp = int(input("Your choice: "))
    except Exception as e:
        print("Invalid Input")
        continue
    if temp not in [1, 2, 3]:
        print("Invalid Input")
        continue
    user_choice = lst[temp - 1]
    random_choice = random.choice(lst)
    print(f"You choose: {user_choice}, Computer choose: {random_choice}")
    if user_choice == "Stone" and random_choice == "Paper":
        print("Computer wins")
        com_points += 1
        print(f"Your score: {user_points},  Computer score: {com_points}")
    elif user_choice == "Stone" and random_choice == "Scissor":
        print("You wins")
        user_points += 1
        print(f"Your score: {user_points},  Computer score: {com_points}")
    elif user_choice == "Paper" and random_choice == "Stone":
        print("You wins")
        user_points += 1
        print(f"Your score: {user_points},  Computer score: {com_points}")
    elif user_choice == "Paper" and random_choice == "Scissor":
        print("Computer wins")
        com_points += 1
        print(f"Your score: {user_points},  Computer score: {com_points}")
    elif user_choice == "Scissor" and random_choice == "Stone":
        print("Computer wins")
        com_points += 1
        print(f"Your score: {user_points},  Computer score: {com_points}")
    elif user_choice == "Scissor" and random_choice == "Paper":
        print("You wins")
        user_points += 1
        print(f"Your score: {user_points},  Computer score: {com_points}")
    else:
        print("It's a tie.")
        print(f"Your score: {user_points},  Computer score: {com_points}")
    Round += 1
print("--Final Result--")
print(f"Your score: {user_points},  Computer score: {com_points}")
if user_points == com_points:
    print("It's a tie.")
elif user_points > com_points:
    print(f"You Wins by {user_points - com_points} points.")
else:
    print(f"Computer Wins by {com_points - user_points} points.")
print("Thanks for playing.")
a = input()

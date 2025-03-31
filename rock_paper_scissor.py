# rock_paper_scissor simple game

# Author: Lasantha Wijewardhana
# Date : 31.03.2025

import random

print("Welcome to Simple Rock, paper, Scissor game!")

# Play game
are_play = input("Do you want to Play: ").lower()

if are_play != "yes":
    quit()

name = input("Enter Your name: ")

computer_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]

# while loops for process
while True:

    user_inputs = input("Enter Rock/Paper/Scissors or Q for quit: ").lower()

    # if condision for quit
    if user_inputs == "q":
        break

    # if condition for continue
    if user_inputs not in options:
        continue

    random_number = random.randint(0, 2)  # random number for options list

    # pick the random number according to list
    computer_pick = options[random_number]

    print("Computer pick " + str(computer_pick))

    # check the conditions for decide win
    if user_inputs == "rock" and computer_pick == "scissors":
        print("Congrates, You Won!!")
        user_wins += 1

    elif user_inputs == "paper" and computer_pick == "rock":
        print("Congrates, You Won!!")
        user_wins += 1

    elif user_inputs == "scissors" and computer_pick == "paper":
        print("Congrates, You Won!!")
        user_wins += 1

    else:
        print("Congrates, Computer Won!!")
        computer_wins += 1

# end outputs
print("You Won " + str(user_wins) + " times.")
print("Computer Won " + str(computer_wins) + " times. \n")

# check the conditions for who the winner
if computer_wins < user_wins:
    print(name + " You won the Game!!!")

else:
    print("Computer won the Game!!!")

print("Good Bye!")

# On day 12, we are: Studying the Global&Local Scope and Making a Little Game

# Project 12 - Number Guessing Game

# Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

logo = """
  ________                            ._.
 /  _____/ __ __   ____   ______ _____| |
/   \  ___|  |  \_/ __ \ /  ___//  ___/ |
\    \_\  \  |  /\  ___/ \___ \ \___ \ \|
 \______  /____/  \___  >____  >____  >__
        \/            \/     \/     \/ \/
"""
print(logo)


def input_validation():
    while not is_valid:
        global player_guess
        player_guess = int(input("I think the computer picked...\t"))
        if player_guess > 100 or player_guess < 0:
            print("You picked an invalid number, try again!")
        else:
            break


def check_answer():
    genie_time = random.randint(2023, 2100)
    global attempt_number
    if player_guess == computer_guess:
        print(f"Computer guessed:\t{computer_guess}\nYou guessed:\t{player_guess}")
        print(
            f"You guessed it correct! You won 1000 wishes! The genie will visit you in the year of {genie_time} to "
            f"grant your wishes :)")
        return 1
    elif player_guess > computer_guess:
        print("Oh no... You guessed it too high... Try something smaller -_-")
        attempt_number -= 1
        print(f"You have {attempt_number} attempts to guess the number")
    elif player_guess < computer_guess:
        print("Oh no... You guessed it too low... Try something bigger -_-")
        attempt_number -= 1
        print(f"You have {attempt_number} attempts to guess the number")


def choose_difficulty():
    global attempt_number

    while attempt_number == -1:
        difficulty_level = input("Type 'easy' for easy mode and type 'hard' for hard mode:\t").lower()
        if difficulty_level == "easy":
            attempt_number = 10
            print("You have 10 attempts to guess the number.\nGood luck!")
        elif difficulty_level == "hard":
            attempt_number = 5
            print("You have 5 attempts to guess the number.\nGood luck!")
        else:
            print("Invalid input, try again!")


def computer():
    return random.randint(0, 100)


print("Welcome to number guessing game! Computer picked a number between 1 and 100. Can you guess what number is it?")
is_valid = False
is_guessed = False
player_guess = 0
attempt_number = -1
computer_guess = computer()

while not is_guessed:
    if attempt_number == 0:
        print(f"You are out of luck and attempts :/\nComputer guessed:\t{computer_guess}\nYou lose!")
        play_again = input("Do you want to play again? [y/n]\t").lower()
        if play_again != "y":
            print("Goodbye")
            break
        attempt_number = -1
        computer_guess = computer()
    else:
        choose_difficulty()
        input_validation()
        is_guessed = check_answer()

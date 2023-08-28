# On day 14, we are: Building a Game and Reviewing the Concepts We've Learned So Far

# Project 14 - Higher/Lower Game
import random
from gamedata_higher_lower import data
from art_higher_lower import logo, versus

print(logo)
print(
    "Welcome to Higher or Lower game!\nWe are gonna present you two public figures and ask you to guess...\nIs the upper one has higher or lower followers than the below one?")


def input_validation(current_figure):
    while True:
        guess = input(f"has Higher or Lower followers than {data[current_figure]['name']}:\t").lower()
        if guess == "higher" or guess == "lower":
            return guess
        else:
            print("Invalid input, try again!")


def check_answer(current_figure, asked_figure, player_score, high_score):
    player_guess = input_validation(current_figure)
    if player_guess == "higher" and data[current_figure]['follower_count'] < data[asked_figure]['follower_count']:
        print("That is correct!")
        print(
            f"{data[asked_figure]['name']}, a/an {data[asked_figure]['description']}, from {data[asked_figure]['country']} has {data[asked_figure]['follower_count']} million followers")
        player_score += 1
    elif player_guess == "lower" and data[current_figure]['follower_count'] > data[asked_figure]['follower_count']:
        print("That is correct!")
        print(
            f"{data[asked_figure]['name']}, a/an {data[asked_figure]['description']}, from {data[asked_figure]['country']} has {data[asked_figure]['follower_count']} million followers")
        player_score += 1
    else:
        print("Oh no! That is incorrect!")
        print(
            f"{data[asked_figure]['name']}, a/an {data[asked_figure]['description']}, from {data[asked_figure]['country']} has {data[asked_figure]['follower_count']} million followers")
        print(f"Game over :/\tYour score: {player_score}\tHighest score in this session: {high_score}")
        return 1, player_score, high_score
    if player_score > high_score:
        high_score = player_score
    print(f"Your score: {player_score}\tHighest score in this session: {high_score}")
    input("Press anything to continue...")
    print("\n" * 50)
    return 0, player_score, high_score


def present(current_figure, asked_figure):
    print("-" * 50)
    print(
        f"{data[current_figure]['name']}, a/an {data[current_figure]['description']}, from {data[current_figure]['country']}...")
    print(f"has {data[current_figure]['follower_count']} million followers. ")
    print(versus)
    print(
        f"{data[asked_figure]['name']}, a/an {data[asked_figure]['description']}, from {data[asked_figure]['country']}...")
    print("-" * 50)


is_start = True

current_figure = random.randint(0, len(data) - 1)
player_score, high_score = 0, 0

def play(is_start, current_figure, player_score, high_score):
    while is_start:
        start_game = input("Do you want to play? [y/n]\t").lower()
        if start_game != "y":
            print("Goodbye")
            return
        print("\n" * 50)
        is_start = False
        break

    asked_figure = random.randint(0, len(data) - 1)
    present(current_figure, asked_figure)
    is_start, player_score, high_score = check_answer(current_figure, asked_figure, player_score, high_score)
    if is_start == 0:
        current_figure = asked_figure
    else:
        player_score = 0
        current_figure = random.randint(0, len(data) - 1)
    play(is_start, current_figure, player_score, high_score)


play(is_start, current_figure, player_score, high_score)

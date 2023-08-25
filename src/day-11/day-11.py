# On day 11, we are: Coding the Capstone Project

# Project 11 - Blackjack
# Didn't use any of the tips B)
import random
import blackjack_art

print(blackjack_art.logo)


def draw_card(deal_times: int):
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealt_cards = list()

    for i in range(deal_times):
        chosen_card = random.choice(all_cards)
        dealt_cards.append(chosen_card)
    return dealt_cards


def calculate_score(deck):
    score = 0
    for card in deck:
        score += card
    return score


def determine_winner(player_deck, computer_deck, player_score, computer_score):
    if player_score > computer_score:
        print(
            f"Your cards:\t{player_deck}\tCurrent score:\t{player_score}")
        print(
            f"Computer's cards:\t{computer_deck}\tComputer score:\t{computer_score}")
        print("You are the closest to 21. You win!")
    elif player_score < computer_score:
        print(
            f"Your cards:\t{player_deck}\tCurrent score:\t{player_score}")
        print(
            f"Computer's cards:\t{computer_deck}\tComputer score:\t{computer_score}")
        print("Computer is the closest to 21. You lose!")
    else:
        print(
            f"Your cards:\t{player_deck}\tCurrent score:\t{player_score}")
        print(
            f"Computer's cards:\t{computer_deck}\tComputer score:\t{computer_score}")
        print("Computer's and your scores are the same. It's a draw!")
    play_again()


def computer_below_seventeen(computer_deck, computer_score, player_deck, player_score):
    while computer_score < 17:
        computer_deck.extend(draw_card(1))
        computer_score = calculate_score(computer_deck)
        if computer_score > 21:
            print(
                f"Your cards:\t{player_deck}\tCurrent score:\t{player_score}")
            print(
                f"Computer's cards:\t{computer_deck}\tComputer score:\t{computer_score}")
            print("Computer went over 21. You win!")
            play_again()
    return computer_deck, computer_score

def play_again():
    play_again = input("Do you want to play again? [y/n]\t").lower()
    if play_again == "y":
        print("\n" * 100)
        play()
    else:
        print("Goodbye")
        exit()

def play():
    player_deck, computer_deck = draw_card(2), draw_card(2)
    player_score, computer_score = calculate_score(player_deck), calculate_score(computer_deck)
    print(
        f"Your cards:\t{player_deck}\tCurrent score:\t{player_score}")
    print(f"Computer's first card:\t{computer_deck[0]}")
    get_card = input("Type 'y' to get another card, type 'n' to pass:\t").lower()

    if get_card == "y":
        player_deck.extend(draw_card(1))
        player_score = calculate_score(player_deck)
        if player_score > 21:
            print(
                f"Your cards:\t{player_deck}\tCurrent score:\t{player_score}")
            print(
                f"Computer's cards:\t{computer_deck}\tComputer score:\t{computer_score}")
            print("You went over 21. You lose!")
            play_again()
    computer_deck, computer_score = computer_below_seventeen(computer_deck, computer_score, player_deck,
                                                             player_score)
    determine_winner(player_deck, computer_deck, player_score, computer_score)


start_game = input("Welcome! Do you want to play a game of Blackjack? Type 'y' or 'n':\t").lower()

if start_game == "y":
    play()
else:
    print("Goodbye")

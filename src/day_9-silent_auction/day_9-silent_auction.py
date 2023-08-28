# On day 9, we are: Studying Dictionaries and Nesting with Lists&Dictionaries

# Project 9 - Secret Auction
import auction_art

auction = {}


def make_bid(name, bid_amount):
    auction[name] = bid_amount


def select_winner(auction):
    winner_amount = 0
    winner = ""

    for name in auction:
        if auction[name] > winner_amount:
            winner_amount = auction[name]
            winner = name
    print("\n" * 50)
    print("And the winner is...")
    print(f"{winner} with a bid of ${winner_amount}.")


print(auction_art.logo)
print("Welcome to the secret auction program.")
is_continue = "yes"

while is_continue == "yes":  # Maybe make this a boolean state instead of string
    name = input("What is your name?\t")
    bid_amount = float(input("What's your bid?\t$"))
    is_continue = input("Are there any other bidders? [yes/no]\t").lower()
    make_bid(name, bid_amount)
    if is_continue == "yes":
        print("\n" * 50)

select_winner(auction)

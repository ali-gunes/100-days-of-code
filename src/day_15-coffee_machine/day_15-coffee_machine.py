from art_coffee_machine import logo
from constants_coffee_machine import MENU, resources

available_options = ["espresso", "latte", "cappuccino"]
total_earnings = 0
current_resource = resources
total_inserted_coins = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0,
}


def coffee_validation():
    """
    Controls the user input for coffee selection and other functionalities like report and off
    """
    while True:
        selected_coffee = input("What would you like? (espresso/latte/cappuccino):\t").lower()
        if selected_coffee in available_options:
            print(f"You've chosen {selected_coffee.title()}")
            return 1, selected_coffee
        elif selected_coffee == "off":
            # For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine
            # shut down the machine
            return 0, selected_coffee
        elif selected_coffee == "report":
            print("Here are the current remaining resources")
            for resource in current_resource:
                print(f"{resource.title()}: {current_resource[resource]} g/ml/$")
            print("Here are the total inserted coins")
            for coins in total_inserted_coins:
                print(f"{coins.title()}: {total_inserted_coins[coins]}")
            input("Press anything to continue...")
            return 1, selected_coffee
        elif selected_coffee == "supply":
            print("Here are the current remaining resources")
            for resource in current_resource:
                print(f"{resource.title()}: {current_resource[resource]}")
            current_resource["water"] += int(input("How much water in milliliters?\t"))
            current_resource["milk"] += int(input("How much milk in milliliters?\t"))
            current_resource["coffee"] += int(input("How much coffee in grams?\t"))
        elif selected_coffee == "collect":
            print("Here is how much the machine profited:\t", current_resource["profit"])
            is_sure = input("Are you sure you want to collect the earnings? [y/n]\t").lower()
            if is_sure == "y":
                current_resource["profit"] = 0
                print("You've collected all the earnings")
                print("Current amount of money in the machine is:\t", current_resource["profit"])
            else:
                print("Goodbye")
        elif selected_coffee == "secrets":
            print("Here are the admin secrets for extra functionality")
            print("'off':\t\tShuts down the machine")
            print("'report':\tGives you a detailed report about how much resources left, your profit and total inserted coins")
            print("'supply':\tYou can supply the machine resources")
            print("'collect':\tAllows you to collect all the profits you've made")
            print("'secrets':\tShows you the machine secrets")
        else:
            print("Invalid input, try again!")


def check_resources(selected_coffee, current_resource):
    """
    Checks if there is enough resources for the selected coffee and outputs the user
    """
    if selected_coffee in available_options:
        for ingredient, value in MENU[selected_coffee]["ingredients"].items():
            if current_resource[ingredient] < value:
                print(
                    f"Currently we don't have enough {ingredient} in the machine to make {selected_coffee}. Please try again later. Sorry for the inconvenience :/")
                input("Press anything to continue...")
                return 0
        return 1


def insert_coin(selected_coffee, total_earnings, total_inserted_coins):
    """
    Controls the inserted coin amount and equivalent value, checks if it's enough for selected coffee, outputs the relevant info to user and logs the earnings
    """
    total_value = 0
    print(f"{selected_coffee.title()}'s current cost is {MENU[selected_coffee]['cost']}$, please insert coins.")
    quarters = int(input("How many quarters:\t"))
    dimes = int(input("How many dimes:\t"))
    nickles = int(input("How many nickles:\t"))
    pennies = int(input("How many pennies:\t"))

    total_value += (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    if total_value >= MENU[selected_coffee]['cost']:
        print(f"You've inserted {'{:.2f}'.format(total_value)}$, enough money to buy your {selected_coffee}. Coming right up!")
        if total_value > MENU[selected_coffee]['cost']:
            difference = total_value - MENU[selected_coffee]['cost']
            print(f"Your excess {'{:.2f}'.format(difference)}$ will be refunded.")
        total_earnings += MENU[selected_coffee]['cost']
        total_inserted_coins["quarters"] += quarters
        total_inserted_coins["dimes"] += dimes
        total_inserted_coins["nickles"] += nickles
        total_inserted_coins["pennies"] += pennies
        return total_value, total_earnings, total_inserted_coins
    else:
        print("Insufficient funds, please insert your coins again!")
        insert_coin(selected_coffee, total_earnings, total_inserted_coins)


def serve_coffee(selected_coffee, current_resource):
    """
    Serves the coffee to user, subtracts the amount from resources
    """
    for ingredient, value in MENU[selected_coffee]["ingredients"].items():
        current_resource[ingredient] -= value
    print(f"Here is your {selected_coffee} ☕. Enjoy!")
    return current_resource


while True:
    print(logo)
    print("Welcome to Caffeine Corner!")
    print("Type 'secrets' to see admin secrets")
    power, selected_coffee = coffee_validation()
    if power != 1:
        print("\n" * 50)
        print("Coffee Machine is shutting down...\nGoodbye")
        break
    is_enough = check_resources(selected_coffee, current_resource)
    if is_enough:
        total_value, total_earnings, total_inserted_coins = insert_coin(selected_coffee, total_earnings,
                                                                        total_inserted_coins)
        current_resource["profit"] = f"${total_earnings}"
        current_resource = serve_coffee(selected_coffee, current_resource)
        answer = input("Do you want to get another coffee? [y/n]\t").lower()
        if answer != "y":
            print("Goodbye")
            break
    print("\n" * 50)

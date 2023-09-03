from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# From here, it's my code
machine_menu = Menu()
machine_maker = CoffeeMaker()
machine_money = MoneyMachine()


def input_validation():
    while True:
        print("\n" * 50)
        print("Welcome to Caffeine Corner!\nPlease select your coffee:")
        selected_coffee = input(f"{machine_menu.get_items()}:\t").lower()
        if selected_coffee in machine_functions:
            current_function = machine_functions[selected_coffee]
            current_function()
        else:
            item = machine_menu.find_drink(selected_coffee)
            if item is not None:
                return item


def off():
    print("\n" * 50)
    print("Machine is shutting down.\nGoodbye.")
    exit()


def show_report():
    print("\n" * 50)
    print("Here is the current report on this session's resources:")
    print("-" * 50)
    machine_maker.report()
    machine_money.report()
    print("-" * 50)
    input("Press anything to continue...")


machine_functions = {
    "off": off,
    "report": show_report,
}

while True:
    selected_coffee = input_validation()
    is_sufficient = machine_maker.is_resource_sufficient(selected_coffee)
    if is_sufficient:
        is_paid = machine_money.make_payment(selected_coffee.cost)
        if is_paid:
            machine_maker.make_coffee(selected_coffee)
    is_continue = input("Do you want to get another coffee? [y/n]\t").lower()
    if is_continue != "y":
        off()

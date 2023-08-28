# On day 10, we are: Studying Functions and Function Outputs (see day 8 for inputs)

# Project 10 - Text Based Calculator

logo = """
 _____________________
|  _________________  |
| | Ali Güneş    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(f_number, l_number):
    return f_number + l_number


def subtract(f_number, l_number):
    return f_number - l_number


def multiply(f_number, l_number):
    return f_number * l_number


def divide(f_number, l_number):
    return f_number / l_number


def exponential(f_number, l_number):
    return f_number ** l_number


def modula(f_number, l_number):
    return f_number % l_number


operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "exp": exponential,
    "mod": modula,
}

print(logo)
print("Welcome to calculator!")
f_number = None
is_finished = False
all_operations = ""
for operation in operation_dict:
    all_operations += f"{operation}\t\t"
while not is_finished:
    if f_number is None:
        f_number = float(input("What is the first number?\t"))

    print(all_operations)
    operation = input("What is the operation?\t").lower()
    if operation not in operation_dict.keys():
        print("Invalid operation, goodbye")
        exit()
    l_number = float(input("What is the second number?\t"))

    result_func = operation_dict[operation]
    result = result_func(f_number, l_number)

    print(f"{f_number} {operation} {l_number} = {result}")
    next_move = input(
        f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'x' to exit:\t").lower()
    if next_move == "y":
        f_number = result
    elif next_move == "x":
        print("Goodbye")
        is_finished = True
    elif next_move == "n":
        f_number = None
        is_finished = False
    else:
        print("Invalid input, try again with a new calculation.")

# On day 5, we are: Studying Loops

# Project 5 - Password Generator: Generate a random password with prompted number of symbols and numbers, shuffle the
# password string
import random

print("Welcome to the  Password Generator!")

password_length = int(input("How many letters would you like in your password?\t"))
symbol_count = int(input("How many symbols would you like?\t"))
number_count = int(input("How many numbers would you like?\t"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

generated_password = ""

if password_length < 0 or number_count < 0 or symbol_count < 0:
    print("Your length needs to be at least 0, try again.")
else:
    # I can rewrite this section with random.choice() but I like the traditional ways
    for symbol in range(0, symbol_count):
        generated_password += symbols[random.randrange(0, len(symbols))]
    for number in range(0, number_count):
        generated_password += numbers[random.randrange(0, len(numbers))]
    for letter in range(0, password_length):
        generated_password += letters[random.randrange(0, len(letters))]

    # Randomize/shuffle the password
    # I could also use the random.shuffle()
    generated_password = "".join(random.sample(generated_password, len(generated_password)))
    print(generated_password)

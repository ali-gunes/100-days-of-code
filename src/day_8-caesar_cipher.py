# On day 8, we are: Studying Functions and Function Inputs

# Project 8 - Caesar Cipher
# I finished this without any help, without seeing the steps and without even looking to Google :) good for me
# Step 1
# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#   and print the encrypted text. e.g. plain_text = "hello" shift = 5 cipher_text = "mjqqt" print output:
#   "The encoded text is mjqqt"
# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# ^ It exceed the index range so I added a little something ^
# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#   message.

# Step 2
# TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
#   amount and print the decrypted text.
# TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#   Then call the correct function based on that 'direction' variable. You should be able to test the code to
#   encrypt *AND* decrypt a message.

# Step 3
# Didn't do these to-do's because I do lots of if/else checks in my functions, I can't merge them.
# - NVM found another way
# TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar().
# TODO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# Step 4
# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#   Try running the program and entering a shift number of 45.
#   Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#   Hint: Think about how you can use the modulus (%).
# TODO-9: What happens if the user enters a number/symbol/space?
#   Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# TODO-10: Can you figure out a way to ask the user if they want to restart the cipher program?


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
# I just check if the char not in alphabet, so I commented out below 2 lines
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '\'', '"', '?', ':']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


# def encrypt(text: str, shift: int) -> None:
#     encrypted_text = []
#     for char in text:
#         # For every char in the text, I found the index in the alphabet and added shift integer, found the new char in
#         # alphabet list and appended to encrypted_char list
#         if char in numbers or char in symbols or char == " ":
#             encrypted_text.append(char)
#         elif alphabet.index(char) + shift >= len(alphabet):
#             excess_char = (alphabet.index(char) + shift) % len(alphabet)
#             encrypted_text.append(alphabet[excess_char])
#         else:
#             encrypted_text.append(alphabet[alphabet.index(char) + shift])
#     print(f"The encoded text is:\t{''.join(encrypted_text)}")
#
#
# def decrypt(text: str, shift: int) -> None:
#     decrypted_text = []
#     for char in text:
#         if char in numbers or char in symbols or char == " ":
#             decrypted_text.append(char)
#         elif alphabet.index(char) - shift <= len(alphabet):
#             excess_char = (alphabet.index(char) - shift) % len(alphabet)
#             decrypted_text.append(alphabet[excess_char])
#         else:
#             decrypted_text.append(alphabet[alphabet.index(char) - shift])
#     print(f"The decoded text is:\t{''.join(decrypted_text)}")

# I combined the encrypt/decrypt functions to avoid DRY (DON'T REPEAT YOURSELF)
def caesar(text, shift, direction) -> None:
    end_text = []
    if direction == "decode":
        shift *= -1  # Subtracting shift if direction is decode
    for char in text:
        # For every char in the text, I found the index in the alphabet and added shift integer, found the new char in
        # alphabet list and appended to encrypted_char list
        if char not in alphabet:
            end_text.append(char)
        elif alphabet.index(char) + shift >= len(alphabet):
            excess_char = (alphabet.index(char) + shift) % len(alphabet)
            end_text.append(alphabet[excess_char])
        else:
            end_text.append(alphabet[alphabet.index(char) + shift])
    print(f"The {direction}d text is:\t{''.join(end_text)}")


print(logo)

is_continue = "y"
while is_continue == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    allowed_directions = ["encode", "decode"]
    # if direction == "encode":
    #     encrypt(text, shift)
    # elif direction == "decode":
    #     decrypt(text, shift)
    # else:
    #     print("Invalid command!")

    if direction not in allowed_directions:
        print("Invalid input, you are leaving.")
        is_continue = "n"
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        is_continue = input("Would you like to go again? [y/n]:\t").lower()

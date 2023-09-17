# On day 26, we are: Learning List Comprehension and Dictionary Comprehension

# Project 26 - NATO Alphabet

import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

# Let's create a dictionary from this CSV file
alphabet = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(alphabet)

name = input("Enter your name to spell in NATO alphabet:\t").upper()

spelled_name = [alphabet[letter] for letter in name]

print(spelled_name)

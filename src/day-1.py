"""
# On day 1, we are: Working with Variables in Python to Manage Data
print("Programming is EPIC\nIt is the closest thing we have as super powers!")

ans = input("Do you agree? [y/n]\t").lower()

if ans == "y":
    print("Yayy! Me too.")
elif ans == "n":
    print("That's unfortunate...")
else:
    print("I don't understand you mate :/")

# Python can take functions in a function
print("Hello", input("What is your name?\t"))
"""

# Band Name Generator: Ask the user for their current city and pet's name, add two each other and print it out
print("Hello, welcome to band name generator\n")
city = input("Where do you currently live?\n")
pet_name = input("What is the name of your pet?\n")
print("*...drum rolls...*\nYour band name is:\t", city + " " + pet_name)


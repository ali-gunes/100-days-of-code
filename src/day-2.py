# On day 2, we are: Understanding Data Types and How to Manipulate Strings

# Tip Calculator: Ask the user for total bill, tip percentage and number of people, return how much each person
# should pay with a 2 decimal point
total_bill = float(input("Welcome to the tip calculator!\nWhat was the total bill?\t$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\t%"))
number_of_people = int(input("How many people to split the bill?\t"))

total_bill = total_bill + (total_bill * tip_percentage / 100)
distributed_bill = round(total_bill / number_of_people, 2)

print(f"Eacnh person should pay:\t${distributed_bill}")

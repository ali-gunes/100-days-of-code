# List Comprehension
digits = [digit for digit in range(10)]
print(digits)

# Exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆
# Write your 1 line code 👇 below:
squared_numbers = [num ** 2 for num in numbers]
# Write your code 👆 above:
print(squared_numbers)

# Exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above
# Write your 1 line code 👇 below:
result = [num for num in numbers if num % 2 == 0]
# Write your code 👆 above:
print(result)

# Dictionary Comrpehension
# Exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# Write your code below:
result = {word: len(word) for word in sentence.split()}
print(result)

# Exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# # 🚨 Don't change code above 👆
# # Write your code 👇 below:
weather_f = {day: (celsius * 9 / 5) + 32 for (day, celsius) in weather_c.items()}
print(weather_f)

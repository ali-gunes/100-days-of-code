import pandas

# Read the csv data
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

# Get the length of each color's corresponding row
cinnamon_color = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
print("Cinnamon Colored Squirrels:", cinnamon_color)

black_color = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print("Black Colored Squirrels:", black_color)

gray_color = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
print("Gray Colored Squirrels:", gray_color)

squirrel_color = {
    "Fur Color": ["Cinnamon", "Black", "Gray"],
    "Count": [cinnamon_color, black_color, gray_color]
}

squirrel_dataframe = pandas.DataFrame(squirrel_color)
squirrel_dataframe.to_csv("squirrel_data_csv")

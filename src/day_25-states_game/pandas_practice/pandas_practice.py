import csv
with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    row_list = list()
    for row in data:
        row_list.append(row)
    for _ in range(1, len(row_list)):
        temperatures.append(int(row_list[_][1]))
    print(temperatures)

# Instead of using CSV lib and writing lots of code, we can just use Pandas
import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"].mean())
print(data.temp.max())

print(data[data.temp == data.temp.max()])  # Get the row with the highest temperature

monday = data[data.day == "Monday"]
print(monday.temp)
f = (monday.temp * 9 / 5) + 32  # Convert Monday's temperature to Fahrenheit from Celsius
print(f)

# Create a dataframe from a dictionary
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
import pandas as pd


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


data = pd.read_csv("2.1 weather_data.csv")
temp_list = data["temp"].to_list()
temp_mean = data["temp"].mean()

temp_max = data["temp"].max()
monday = data[data.day == "Monday"]

monday_temperature = int(monday.temp.iloc[0])

monday_fahrenheit = celsius_to_fahrenheit(monday_temperature)
print(f" The temperature on Monday was {monday_fahrenheit} fahrenheit")

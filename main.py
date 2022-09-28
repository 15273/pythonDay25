# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     list_temp = []
#     for row in data:
#         if row[1] != "temp":
#             list_temp.append(int(row[1]))
#         print(row)
#     print(list_temp)
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "For Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
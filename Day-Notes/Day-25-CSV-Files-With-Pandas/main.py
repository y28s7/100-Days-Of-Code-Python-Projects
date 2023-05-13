# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
#
# # NORMAL CSV DATA ANALYSIS 👇
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# # NORMAL CSV DATA ANALYSIS 👆
#
# # PANDAS CSV DATA ANALYSIS 👇
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # # Find average normally
# # temp_list = data["temp"].to_list()
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
# #
# # # Find average waaaay quicker with same answer
# # print(data["temp"].mean())
# #
# # # Maximum value
# # max_temp = data["temp"].max()
# # print(max_temp)
# #
# # # Get Data in Columns
# # print(data["condition"])
# #
# # # Alternative way from square brackets
# # print(data.condition)
#
# # Get Data in Row
# # print(data[data.day == "Monday"])
# #
# # Get row of the highest temperature
# # print(data[data.temp == data.temp.max()])
#
# # Get another column's data in a specific row
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# #
# # Find temperature of Monday in F
# # print((monday.temp * 9/5) + 32)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "John"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
# # PANDAS CSV DATA ANALYSIS 👆

# SQUIRREL ANALYSIS 👇

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

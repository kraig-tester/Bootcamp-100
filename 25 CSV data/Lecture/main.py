# import csv

# Basic csv library

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

# Documentation https://pandas.pydata.org/docs/
# API https://pandas.pydata.org/docs/reference/index.html
import pandas as pd

data = pd.read_csv("weather_data.csv")

# print(type(data)) # Dataframe a.k.a. table
# print(type(data["temp"])) # Series a.k.a. list

data_dict = data.to_dict() # Conversion from dataframe to dictionary(JSON)
# print(data_dict)

temp_list = data["temp"].to_list() # Conversion series to list
# print(temp_list)

# avg_temp = sum(temp_list)/len(temp_list)
avg_temp = data["temp"].mean()
# print(avg_temp)

# print(data["temp"].max())

# Another way to call columns
# print(data.condition)

# Accessing row
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# # C to F formula (x × 9/5) + 32
# monday_temp_c = monday.temp
# monday_temp_f = (monday_temp_c * 9/5) + 32
# print(str(monday_temp_f))

# Create a dataframe from scratch
student_dict = {
    "students": ["Amy", "James", "Igor"],
    "scores": [80, 70, 89]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

# csv from dataframe
student_df.to_csv("student_data.csv")
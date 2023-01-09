import pandas as pd

PATH_NAME = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

data = pd.read_csv(PATH_NAME)
black_squirels_list = data[data["Primary Fur Color"] == "Black"]
black_squirels_count = len(black_squirels_list)
grey_squirels_list = data[data["Primary Fur Color"] == "Gray"]
grey_squirels_count = len(grey_squirels_list)
red_squirels_list = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirels_count = len(red_squirels_list)

# print(red_squirels_list)
# print(red_squirels_count)

squirrel_count = {
    "color": ["black", "gray", "red"],
    "count": [black_squirels_count,grey_squirels_count,red_squirels_count]
}

squirrel_count_df = pd.DataFrame(squirrel_count)

squirrel_count_df.to_csv("squirrel_count.csv")
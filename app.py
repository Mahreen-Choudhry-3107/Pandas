import pandas as pd

# # read data from CSV file into a DataFrame
# df = pd.read_csv("E:/AI Engineer/Pandas/data.csv", encoding='utf-8')

# print(df)

# # display the first 5 rows of the DataFrame
# print(df.head())


# reading data from an Excel file into a DataFrame
# df_excel = pd.read_excel("E:/AI Engineer/Pandas/data.xlsx")
# print(df_excel)

# read data from a JSON file into a DataFrame
df_json = pd.read_json("E:/AI Engineer/Pandas/data.json", orient='records')
print(df_json)
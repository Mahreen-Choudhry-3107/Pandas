# head() tail()
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head(10))  # Display the first 10 rows of the DataFrame
print(df.tail(10))  # Display the last 10 rows of the DataFrame
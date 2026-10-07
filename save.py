import pandas as pd

data = {
  "Name": ["Mahreen", "Umair", "Ali", "Ayesha"],
  "Age": [19, 20, 21, 22],
  "City": ["Karachi", "Lahore", "Islamabad", "Peshawar"]
}
df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)

# save to excel file

df.to_excel("output.xlsx", index=False)

# save to json file
df.to_json("output.json", orient="records")
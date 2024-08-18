import pandas as pd

df = pd.read_csv("CustomerData.txt")
df["ProductName"] = df["ProductName"].fillna("No Product")

print(df)
df.to_csv("CustomerData.txt", index=False)
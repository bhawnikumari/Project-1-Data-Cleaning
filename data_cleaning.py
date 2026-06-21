import pandas as pd

df = pd.read_csv("raw_data.csv")

df = df.drop_duplicates()

df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning Completed Successfully")
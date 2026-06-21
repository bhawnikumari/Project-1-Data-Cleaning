
import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv("raw_data.csv")

print("Original Dataset Shape:", df.shape)

# ---------------------------
# Missing Value Handling
# ---------------------------

for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include='object').columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

# ---------------------------
# Duplicate Removal
# ---------------------------

duplicate_count = df.duplicated().sum()
print("Duplicate Records Found:", duplicate_count)

df.drop_duplicates(inplace=True)

# ---------------------------
# Date Standardization
# ---------------------------

for col in df.columns:
    if "date" in col.lower():
        df[col] = pd.to_datetime(df[col], errors='coerce')
        df[col] = df[col].dt.strftime('%Y-%m-%d')

# ---------------------------
# Text Standardization
# ---------------------------

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip().str.title()

# ---------------------------
# Numeric Formatting
# ---------------------------

for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].round(2)

# ---------------------------
# Save Cleaned Dataset
# ---------------------------

df.to_csv("cleaned_data.csv", index=False)

print("Data Cleaning Completed Successfully!")
print("Final Dataset Shape:", df.shape)
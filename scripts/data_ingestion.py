import pandas as pd
import os

print("Current Directory:")
print(os.getcwd())


folder = "../data/raw"

for file in os.listdir(folder):

    if file.endswith(".csv"):

        filepath = os.path.join(folder, file)

        print("\n" + "="*60)
        print(f"FILE: {file}")

        df = pd.read_csv(filepath)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())
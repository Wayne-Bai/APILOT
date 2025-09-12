import pandas as pd

# load data from a file
data = pd.read_csv("data.csv")

# compute the first non-null entry of each column
first_non_null = []
for col in data:
    for idx, val in enumerate(col):
        if not pd.isna(val):
            first_non_null.append((idx, val))

print(first_non_null)

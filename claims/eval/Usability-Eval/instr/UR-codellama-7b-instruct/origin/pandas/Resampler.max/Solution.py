
import pandas as pd

# read data from a csv file
df = pd.read_csv("data.csv")

# compute the maximum value of each group
max_values = df.groupby("group").max()

# print the results
print(max_values)

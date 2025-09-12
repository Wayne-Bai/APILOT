
import pandas as pd

# Read in the data from the CSV file
df = pd.read_csv("data.csv")

# Compute the maximum value for each group
max_values = df.groupby(["group"])["value"].max()

# Print the result
print(max_values)

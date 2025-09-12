
import pandas as pd

# Read the data from a csv file
df = pd.read_csv("data.csv")

# Define the number of rows to return
n = 5

# Use the nth_rows method to get the last n rows of the dataframe
last_rows = df.nth_rows(n)

# Print the last n rows
print(last_rows)

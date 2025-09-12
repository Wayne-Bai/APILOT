
import pandas as pd

# Read csv file
df = pd.read_csv("data.csv")

# Get first n rows
first_n_rows = df.head(n)

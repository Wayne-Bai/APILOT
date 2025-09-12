import pandas as pd

# Create a new column in the dataframe with the suffix "S" added to each element
df["new_column"] = df["existing_column"].astype(str) + "S"

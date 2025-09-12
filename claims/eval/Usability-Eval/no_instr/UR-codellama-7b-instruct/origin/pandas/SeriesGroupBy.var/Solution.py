import pandas as pd

# read csv file into a dataframe
df = pd.read_csv("data.csv")

# compute variance for each group, excluding missing values
variance = df.groupby("group").agg(["mean", "count"])["value"].var()

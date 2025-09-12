import pandas as pd

# Load data from a CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv')

# Compute pairwise correlation between all columns in the DataFrame
corr = df.corr()

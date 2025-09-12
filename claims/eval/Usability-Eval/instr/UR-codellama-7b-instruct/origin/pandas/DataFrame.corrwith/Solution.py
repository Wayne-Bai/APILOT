
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv("data.csv")

# Compute pairwise correlation
corr = df.corr()

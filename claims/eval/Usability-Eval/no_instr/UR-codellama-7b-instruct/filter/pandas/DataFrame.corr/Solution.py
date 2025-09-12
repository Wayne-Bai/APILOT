
import pandas as pd

# Load the data from a CSV file
df = pd.read_csv("data.csv")

# Compute the pairwise correlation of all columns in the dataframe, excluding NA/null values
corr_matrix = df.corr(method="pearson", min_periods=1)

# Print the correlation matrix
print(corr_matrix)

import pandas as pd

# Load the dataset into a pandas dataframe
df = pd.read_csv('dataset.csv')

# Compute pairwise correlation of columns, excluding NA/null values
corr = df.corr(method='pearson', min_periods=1)

print(corr)

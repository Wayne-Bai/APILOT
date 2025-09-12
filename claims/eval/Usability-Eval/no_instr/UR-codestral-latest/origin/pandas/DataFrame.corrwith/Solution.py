# Import the pandas library
import pandas as pd

# Assume we have a DataFrame `df`
# df = pd.read_csv('your_data.csv')  # Uncomment this line if you have a CSV file

# Use the corr() function to compute pairwise correlations
correlation_matrix = df.corr()

# Print the correlation matrix
print(correlation_matrix)

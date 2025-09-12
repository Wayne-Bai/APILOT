import pandas as pd

# Assuming `df` is your DataFrame
# If `df` is not yet defined, you would need to load your data
# into a DataFrame, for example:
# df = pd.read_csv('your_data.csv')

# Using the `corr()` function from pandas
correlation_matrix = df.corr()

# Display the correlation matrix
print(correlation_matrix)

import pandas as pd

# Assuming df is your DataFrame
# First, we'll replace missing values with the mean of the column
df_filled = df.fillna(df.mean())

# Then, we'll compute the pairwise correlation matrix
corr_matrix = df_filled.corr()

# Display the correlation matrix
print(corr_matrix)

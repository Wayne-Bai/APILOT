import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to compute the standard error for

# Compute the mean of the column, excluding missing values
mean_value = df['column_name'].dropna().mean()

# Compute the standard error of the mean
std_error = df['column_name'].dropna().std() / len(df)

print("Mean value:", mean_value)
print("Standard Error of the Mean:", std_error)

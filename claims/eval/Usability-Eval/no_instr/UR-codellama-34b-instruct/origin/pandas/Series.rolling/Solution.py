import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# Define the window size and calculation function
window_size = 3
calculation_func = lambda x: x.mean()

# Perform rolling window calculations
rolling_df = df.rolling(window=window_size)
rolling_df['A'] = rolling_df['A'].apply(calculation_func)
rolling_df['B'] = rolling_df['B'].apply(calculation_func)

# Print the result
print(rolling_df)

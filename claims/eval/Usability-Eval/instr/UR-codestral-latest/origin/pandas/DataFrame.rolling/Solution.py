import pandas as pd

# Assuming you have a DataFrame named 'df' and 'value' is the column for which you want to calculate the rolling mean
# Replace 'value' with your column name
df['rolling_mean'] = df['value'].rolling(window=3).mean()

# Print the DataFrame to see the results
print(df)

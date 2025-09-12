import pandas as pd

# Create a sample DataFrame with duplicate values
df = pd.DataFrame({
    'A': [1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6]
})

# Convert the DataFrame to a Series
series = df['A']

# Use the duplicated() function to find duplicate values, 
# then invert the boolean mask to select unique values
unique_series = series[~series.duplicated()]

print(unique_series)

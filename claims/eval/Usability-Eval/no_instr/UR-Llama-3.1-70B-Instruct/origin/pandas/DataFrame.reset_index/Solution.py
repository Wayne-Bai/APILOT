# Import the pandas library
import pandas as pd

# Create a DataFrame with a MultiIndex
data = {
    'City': ['New York', 'Chicago', 'Los Angeles', 'Houston', 'Seattle'],
    'Year': [2020, 2020, 2021, 2020, 2021],
    'Population': [8.4, 2.7, 3.9, 2.3, 0.7]
}
df = pd.DataFrame(data)
df = df.set_index(['City', 'Year'])

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Reset the index
df_reset = df.reset_index()

# Display the DataFrame after resetting the index
print("\nDataFrame after resetting the index:")
print(df_reset)

# Reset a specific level of the index
df_reset_level = df.reset_index(level='Year')

# Display the DataFrame after resetting a specific level of the index
print("\nDataFrame after resetting a specific level of the index:")
print(df_reset_level)

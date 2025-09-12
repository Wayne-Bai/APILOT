import pandas as pd

# Creating a MultiIndex DataFrame
data = {
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad'],
    'Year': [2020, 2020, 2020, 2021, 2021, 2021],
    'Sales': [100, 200, 300, 400, 500, 600]
}

df = pd.DataFrame(data)

# Set 'City' and 'Year' as the index
df = df.set_index(['City', 'Year'])

print("Original DataFrame:")
print(df)

# Reset the index
df_reset = df.reset_index()

print("\nDataFrame after resetting the index:")
print(df_reset)

# If you want to reset a specific level of the index
df_reset_level = df.reset_index(level='City')

print("\nDataFrame after resetting a specific level of the index:")
print(df_reset_level)

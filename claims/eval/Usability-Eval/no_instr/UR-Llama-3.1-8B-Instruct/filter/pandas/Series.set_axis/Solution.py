# Import pandas library
import pandas as pd

# Create a dictionary
data = {'Year': [2010, 2011, 2012, 2013, 2014], 
        'Sales': [100, 120, 140, 160, 180]}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Define a new index
new_index = [2020, 2021, 2022, 2023, 2024]

# Assign the new index to the desired axis (0 for index, 1 for columns)
df.set_axis(index=new_index, axis=0, inplace=True)

# Print the DataFrame with the new index
print("\nDataFrame after assigning new index:")
print(df)

# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19]}
df = pd.DataFrame(data, index=['A', 'B', 'C'])

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Reset the index of the DataFrame
df_reset = df.reset_index()

# Print the DataFrame with the index reset
print("\nDataFrame with the index reset:")
print(df_reset)

# To reset the index and drop the original index column
df_reset_drop = df.reset_index(drop=True)

# Print the DataFrame with the index reset and the original index column dropped
print("\nDataFrame with the index reset and the original index column dropped:")
print(df_reset_drop)

# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Tom', 'Nick', 'Jack', 'Tom', 'John', 'Tom', 'John'],
    'Age': [20, 21, 19, 20, 20, 21, 19]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Drop duplicates and reset index
df_unique = df.drop_duplicates().reset_index(drop=True)

# Print the DataFrame with duplicate values removed
print("\nDataFrame with duplicate values removed:")
print(df_unique)

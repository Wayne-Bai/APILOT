# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Tom', 'Nick', 'John', 'Mike'],
        'Age': [20, 21, 19, 18]}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Assign desired index to the DataFrame
df.index = ['Person1', 'Person2', 'Person3', 'Person4']

# Print the DataFrame with the new index
print("\nDataFrame with new index:")
print(df)

# Assign desired index to the columns
df.columns = ['First_Name', 'Years_Old']

# Print the DataFrame with the new column names
print("\nDataFrame with new column names:")
print(df)

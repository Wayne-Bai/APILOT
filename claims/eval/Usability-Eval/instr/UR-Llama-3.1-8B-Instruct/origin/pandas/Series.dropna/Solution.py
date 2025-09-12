# Import the pandas library
import pandas as pd

# Create a sample DataFrame with missing values
data = {
    'Name': ['John', 'Alice', None, 'Bob', 'Emma'],
    'Age': [25, 31, 42, None, 35]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Fill missing values in the 'Name' column with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')

# Fill missing values in the 'Age' column with 0
df['Age'] = df['Age'].fillna(0)

# Print the DataFrame after filling missing values
print("\nDataFrame after filling missing values:")
print(df)

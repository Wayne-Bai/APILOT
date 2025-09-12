# Import the pandas library
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Create a desired index
desired_index = [10, 15, 20]

# Set the desired index for the 'Name' axis
df.set_index('Name', inplace=True)

# Set the desired index for the 'Age' axis
df['Age'] = pd.to_numeric(desired_index)

# Print the updated DataFrame
print("\nUpdated DataFrame with desired index for 'Age' axis:")
print(df)

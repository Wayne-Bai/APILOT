# Import the pandas library
import pandas as pd

# Create a pandas DataFrame with some data
data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Return the data in the index as a numpy array
data_in_index = df.index.to_numpy()

# Print the data in the index as a numpy array
print("\nData in Index as Numpy Array:")
print(data_in_index)

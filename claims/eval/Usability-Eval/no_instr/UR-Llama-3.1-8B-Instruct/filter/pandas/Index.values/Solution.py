import pandas as pd

# Create a dictionary representing the data
data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'City': ['New York', 'Chicago', 'Los Angeles']
}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Print the data in the Index
print(df.index)

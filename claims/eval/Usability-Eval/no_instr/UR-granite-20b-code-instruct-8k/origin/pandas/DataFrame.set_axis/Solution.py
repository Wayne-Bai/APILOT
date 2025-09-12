import pandas as pd

# Define the data
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}

# Create the DataFrame
df = pd.DataFrame(data)

# Set the desired index
df.set_index('A', inplace=True)

# Display the DataFrame with the new index
print(df)

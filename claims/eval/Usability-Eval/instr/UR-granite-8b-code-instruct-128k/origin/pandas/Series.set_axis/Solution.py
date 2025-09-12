import pandas as pd

# Create a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Set a new index
df.index = ['a', 'b', 'c']

# Display the updated DataFrame
print(df)

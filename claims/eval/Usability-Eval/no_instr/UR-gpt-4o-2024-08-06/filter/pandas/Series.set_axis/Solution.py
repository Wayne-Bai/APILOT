import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Assign a desired index to the DataFrame
desired_index = ['first', 'second', 'third']
df.index = desired_index

# Print the DataFrame to see the result
print(df)

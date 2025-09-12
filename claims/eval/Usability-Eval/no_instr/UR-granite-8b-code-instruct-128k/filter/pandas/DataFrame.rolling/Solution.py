import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [2, 3, 4, 5, 6],
                   'C': [3, 4, 5, 6, 7]})

# Perform a rolling window calculation on the 'A' column
result = df['A'].rolling(window=2).sum()

# Print the result
print(result)

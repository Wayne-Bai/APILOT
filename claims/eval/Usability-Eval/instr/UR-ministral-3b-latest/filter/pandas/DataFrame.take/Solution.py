import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

# Return elements in the 1st, 2nd, 3rd, and 4th columns (0-based indexing) along rows
result = df[['A', 'B', 'A', 'B']]
print(result)

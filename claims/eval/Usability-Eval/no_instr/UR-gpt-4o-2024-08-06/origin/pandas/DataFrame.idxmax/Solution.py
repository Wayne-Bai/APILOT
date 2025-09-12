import pandas as pd

# Sample data for demonstration
data = {
    'A': [1, 2, 1, 4],
    'B': [4, 3, 6, 1],
    'C': [7, 8, 5, 2]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Return index of first occurrence of maximum over requested axis
max_index = df.idxmax(axis=0)  # axis=0 for column-wise; use axis=1 for row-wise

print(max_index)

# Import the pandas library
import pandas as pd

# Create a DataFrame (replace with your actual data)
data = {
    'A': [1, 2, pd.NA, 4, 5],
    'B': [2, pd.NA, 4, 6, pd.NA],
    'C': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# Compute pairwise correlation of columns, excluding NA/null values
correlation_matrix = df.dropna().corr()

print(correlation_matrix)

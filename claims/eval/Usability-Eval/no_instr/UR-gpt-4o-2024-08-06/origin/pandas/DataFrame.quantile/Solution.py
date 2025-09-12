import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
}
df = pd.DataFrame(data)

# Define the quantile you want to compute, e.g., 0.5 for the median
quantile_value = 0.5

# Get the quantile value for each column (axis=0)
quantile_per_column = df.quantile(quantile_value, axis=0)

# Get the quantile value for each row (axis=1)
quantile_per_row = df.quantile(quantile_value, axis=1)

print("Quantile per column:")
print(quantile_per_column)
print("\nQuantile per row:")
print(quantile_per_row)

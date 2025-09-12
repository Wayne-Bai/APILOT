import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# Calculate the 0.25 quantile (25th percentile) over the columns (axis=0)
quantile_values = df.quantile(q=0.25, axis=0)

print(quantile_values)

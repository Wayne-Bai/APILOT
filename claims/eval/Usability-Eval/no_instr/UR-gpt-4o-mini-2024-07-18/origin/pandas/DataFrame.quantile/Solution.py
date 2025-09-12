import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 5, 1, 4]
}

df = pd.DataFrame(data)

# Calculate quantiles along the specified axis (0 for rows, 1 for columns)
quantile_value = df.quantile(q=0.5, axis=0)  # 0.5 quantile (median) across rows
print(quantile_value)

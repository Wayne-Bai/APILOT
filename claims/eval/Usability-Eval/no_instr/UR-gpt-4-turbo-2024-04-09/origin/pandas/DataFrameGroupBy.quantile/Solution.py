import pandas as pd

# Example DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Values': [10, 15, 10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Compute the quantile per group
result = df.groupby('Category')['Values'].quantile(0.5)  # Adjust quantile as needed (0.5 represents the median)
print(result)

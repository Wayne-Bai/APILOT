import pandas as pd

# Creating a sample DataFrame
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [15, 25, 35, 45, 55]
}
df = pd.DataFrame(data)

# Calculating the quantile
quantile_value = df.quantile(0.5)  # 0.5 represents the 50th percentile, also known as the median
print(quantile_value)

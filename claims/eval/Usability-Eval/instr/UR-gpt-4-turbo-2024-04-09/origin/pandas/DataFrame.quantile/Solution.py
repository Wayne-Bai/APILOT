import pandas as pd

# Creating sample data
data = {'value1': [10, 20, 30, 40, 50],
        'value2': [15, 25, 35, 45, 55]}
df = pd.DataFrame(data)

# Define the quantile
quantile_value = 0.5  # Median quantile

# Calculate the quantile over the requested axis (default axis=0, which is 'index')
result = df.quantile(quantile_value)

print(result)

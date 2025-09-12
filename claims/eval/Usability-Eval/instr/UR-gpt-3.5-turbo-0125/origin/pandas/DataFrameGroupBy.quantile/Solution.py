
import pandas as pd

# Sample data
data = {
    'group': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'value': [10, 20, 30, 15, 25, 35, 12, 24, 36]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the quantile(s) you are interested in
quantile_values = [0.25, 0.5, 0.75]

# Calculate the group values at the given quantile
group_quantiles = df.groupby('group')['value'].quantile(q=quantile_values)

print(group_quantiles)


import pandas as pd

# Create a sample dataframe
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# Get the values at a specific quantile (e.g., 0.2) over the rows (axis=0)
quantile_value = df.quantile(0.2, axis=0)

print(quantile_value)

import pandas as pd

# Assume we have a DataFrame df
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [100, 200, 300, 400, 500],
    'C': ['a', 'b', 'c', 'd', 'e']
})

# For example, If we want to find the 0.5 quantile over axis 0, we do:
quantile_0_5_axis_0 = df.quantile(0.5, axis=0)

# If we want to find the 0.5 quantile over axis 1, we do:
quantile_0_5_axis_1 = df.quantile(0.5, axis=1)

print("Quantile at 0.5 over axis 0: \n", quantile_0_5_axis_0)
print("Quantile at 0.5 over axis 1: \n", quantile_0_5_axis_1)

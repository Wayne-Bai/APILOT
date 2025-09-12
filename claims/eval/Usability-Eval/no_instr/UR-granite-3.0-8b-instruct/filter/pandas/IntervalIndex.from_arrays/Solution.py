import pandas as pd

# Assuming left_bounds and right_bounds are your arrays
left_bounds = [1, 3, 5]
right_bounds = [2, 4, 6]

# Create a DataFrame
df = pd.DataFrame({
    'left_bound': left_bounds,
    'right_bound': right_bounds
})

# Print the DataFrame
print(df)

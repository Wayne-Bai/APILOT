import pandas as pd

# Assuming the left and right bounds are in two separate arrays
left_bounds = [1, 3, 5, 7, 9]
right_bounds = [2, 4, 6, 8, 10]

# Create a DataFrame with the left and right bounds
df = pd.DataFrame({
    'Left Bound': left_bounds,
    'Right Bound': right_bounds
})

# Print the DataFrame
print(df)

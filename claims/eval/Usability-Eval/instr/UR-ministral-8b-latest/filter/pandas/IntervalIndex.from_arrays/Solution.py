import pandas as pd

# Define the left bounds
left_bounds = [1, 2, 3, 4, 5]

# Define the right bounds
right_bounds = [10, 20, 30, 40, 50]

# Create dataframes for left and right bounds
df_left_bounds = pd.DataFrame(left_bounds, columns=['Left Bound'])
df_right_bounds = pd.DataFrame(right_bounds, columns=['Right Bound'])

# Print the dataframes
print("Left Bounds:\n", df_left_bounds)
print("\nRight Bounds:\n", df_right_bounds)

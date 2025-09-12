import pandas as pd

# Defining the left and right bounds
left_bounds = [1, 2, 3, 4, 5]
right_bounds = [10, 20, 30, 40, 50]

# Creating a DataFrame to represent the bounds
bounds_df = pd.DataFrame({
    'Left Bound': left_bounds,
    'Right Bound': right_bounds
})

print(bounds_df)

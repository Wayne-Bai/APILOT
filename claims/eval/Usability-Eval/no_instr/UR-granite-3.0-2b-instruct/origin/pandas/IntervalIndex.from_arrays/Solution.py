import pandas as pd

# Create two arrays defining the left and right bounds
left_bounds = [1, 3, 5, 7, 9]
right_bounds = [2, 4, 6, 8, 10]

# Create a pandas DataFrame
df = pd.DataFrame({
    'Left Bound': left_bounds,
    'Right Bound': right_bounds
})

# Print the DataFrame
print(df)

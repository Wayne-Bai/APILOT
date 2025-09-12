import pandas as pd

# Example arrays defining the left and right bounds
left_bounds = [1, 3, 5, 7]
right_bounds = [2, 4, 6, 8]

# Create a DataFrame from the arrays
df = pd.DataFrame({
    'left_bound': left_bounds,
    'right_bound': right_bounds
})

# Display the DataFrame
print(df)

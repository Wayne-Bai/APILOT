import pandas as pd

# Define the left and right bounds arrays
left_bounds = [1, 3, 5, 7]
right_bounds = [2, 4, 6, 8]

# Create a DataFrame from the bounds arrays
df = pd.DataFrame({
    'left_bound': left_bounds,
    'right_bound': right_bounds
})

# Display the DataFrame
print(df)

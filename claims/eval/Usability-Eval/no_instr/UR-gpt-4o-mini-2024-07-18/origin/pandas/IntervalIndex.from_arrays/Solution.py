import pandas as pd

# Define the left and right bounds
left_bounds = [1, 2, 3, 4]
right_bounds = [5, 6, 7, 8]

# Create a DataFrame using the bounds
df = pd.DataFrame({
    'Left': left_bounds,
    'Right': right_bounds
})

print(df)

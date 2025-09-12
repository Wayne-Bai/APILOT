import pandas as pd

# Example data: left and right bounds
left_bounds = [1, 3, 5]
right_bounds = [2, 4, 6]

# Create a DataFrame using the bounds
df = pd.DataFrame({
    'Left': left_bounds,
    'Right': right_bounds
})

print(df)

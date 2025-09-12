import pandas as pd

# Sample data arrays defining left and right bounds
left_bounds = [1, 3, 5]
right_bounds = [2, 4, 6]

# Constructing a DataFrame using the two arrays
df = pd.DataFrame({
    'Left': left_bounds,
    'Right': right_bounds
})

# Displaying the DataFrame
print(df)

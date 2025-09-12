import pandas as pd

# Example arrays defining the left and right bounds
left_bounds = [1, 10, 20]
right_bounds = [5, 15, 25]

# Constructing a DataFrame using the two arrays
df_bounds = pd.DataFrame({'Left': left_bounds, 'Right': right_bounds})

print(df_bounds)

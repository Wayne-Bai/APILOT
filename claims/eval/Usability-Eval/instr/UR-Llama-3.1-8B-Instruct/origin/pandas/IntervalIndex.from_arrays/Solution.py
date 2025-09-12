import pandas as pd

# Create the left bound array
left_bounds = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create the right bound array
right_bounds = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a DataFrame with the left and right bounds
df = pd.DataFrame({
    'Left Bound': left_bounds,
    'Right Bound': right_bounds
})

# Use the Merge function to join the arrays
merged_bounds = df.merge(
    df.assign(mTableRowValue=range(len(left_bounds))),
    left_index=True,
    right_index=True,
    how='inner',
    suffixes=('_left', '_right')
)

# Display the result
print(merged_bounds)

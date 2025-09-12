import pandas as pd

# Create two arrays with the left and right bounds
left_bounds = np.array([10, 20, 30, 40])
right_bounds = np.array([50, 60, 70, 80])

# Construct a DataFrame with the two arrays as columns
df = pd.DataFrame({'left': left_bounds, 'right': right_bounds})

print(df)

import pandas as pd

# Assuming left and right bounds are numpy arrays
left_bounds = np.array([1, 2, 3])
right_bounds = np.array([4, 5, 6])

# Construct a DataFrame from the arrays
df = pd.DataFrame({'Left_Bound': left_bounds, 'Right_Bound': right_bounds})

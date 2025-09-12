
import pandas as pd

left_bounds = [1, 2, 3, 4, 5]
right_bounds = [10, 20, 30, 40, 50]

bounds_df = pd.DataFrame({'left_bound': left_bounds, 'right_bound': right_bounds})
print(bounds_df)

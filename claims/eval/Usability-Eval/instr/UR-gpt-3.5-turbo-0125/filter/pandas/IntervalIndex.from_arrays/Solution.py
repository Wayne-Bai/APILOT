
import pandas as pd

left_bounds = [1, 3, 5, 7, 9]
right_bounds = [2, 4, 6, 8, 10]

df = pd.DataFrame({'left_bound': left_bounds, 'right_bound': right_bounds})
print(df)

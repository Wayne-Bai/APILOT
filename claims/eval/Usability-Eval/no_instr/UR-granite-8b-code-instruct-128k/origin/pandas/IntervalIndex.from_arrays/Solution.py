import pandas as pd

left_bounds = [1, 2, 3]
right_bounds = [4, 5, 6]

df = pd.DataFrame({'left': left_bounds, 'right': right_bounds})
print(df)

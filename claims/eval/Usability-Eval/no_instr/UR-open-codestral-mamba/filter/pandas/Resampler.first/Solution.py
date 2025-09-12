import pandas as pd

# Assume we have the following DataFrame
# df = pd.DataFrame({
#     'A': [None, 2, None, 4, None],
#     'B': [5, None, None, None, None],
#     'C': [None, None, 3, 4, 5],
# })

# Use the cumulative minimum (cummin) to find the first non-null entry
result = df.cummin().idxmin()

print(result)

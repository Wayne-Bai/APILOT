import pandas as pd
s = pd.Series([1, 2, 3, 4, 5], index=[10, 20, 30, 40, 50])
print(s.first_valid_index())


import pandas as pd
s = pd.Series([1, 2, None, 4, 5])
result = s.first_valid_index()
print(result)

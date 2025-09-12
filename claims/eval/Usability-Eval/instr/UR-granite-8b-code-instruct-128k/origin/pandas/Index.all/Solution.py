
import pandas as pd
def all_elements_truthy(series):
 return all(series)
series = pd.Series([True, True, True])
print(all_elements_truthy(series)) # Output: True

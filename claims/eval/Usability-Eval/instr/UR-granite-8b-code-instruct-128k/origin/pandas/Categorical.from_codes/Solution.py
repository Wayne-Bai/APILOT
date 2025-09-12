import pandas as pd
categories = ['A', 'B', 'C']
codes = [0, 1, 2]
categorical = pd.Categorical.from_codes(codes, categories)
print(categorical)

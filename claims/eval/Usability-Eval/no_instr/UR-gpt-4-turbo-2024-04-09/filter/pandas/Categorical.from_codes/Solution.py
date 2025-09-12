import pandas as pd

codes = [0, 1, 2, 0, 1, 2]
categories = ['red', 'blue', 'green']

categorical_data = pd.Categorical.from_codes(codes, categories)

print(categorical_data)

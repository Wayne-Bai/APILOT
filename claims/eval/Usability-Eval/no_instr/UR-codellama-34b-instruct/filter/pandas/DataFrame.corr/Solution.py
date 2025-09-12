
import pandas as pd

# create sample data
data = {'A': [1, 2, 3, 4], 'B': [4, 5, 6, 7], 'C': [8, 9, 10, 11]}
df = pd.DataFrame(data)

# compute pairwise correlation of columns while excluding NA/null values
corr_matrix = df.corr()
print(corr_matrix)

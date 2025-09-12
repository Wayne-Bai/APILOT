import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, None],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, 3, None, 4]
}
df = pd.DataFrame(data)

# Compute pairwise correlation of columns, excluding NA/null values
corr = df.corr()
print(corr)

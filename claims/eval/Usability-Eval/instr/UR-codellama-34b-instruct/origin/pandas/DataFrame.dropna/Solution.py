import pandas as pd

# create a sample dataframe with missing values
data = {'Name': ['Alice', 'Bob', None],
        'Age': [25, 30, None]}
df = pd.DataFrame(data)

# remove rows with missing values
df.dropna()

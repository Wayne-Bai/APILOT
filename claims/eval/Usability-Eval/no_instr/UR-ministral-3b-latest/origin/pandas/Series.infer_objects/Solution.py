import pandas as pd

# Example dataframe
df = pd.DataFrame({
    'column1': ['A', 'B', 'C', 'D'],
    'column2': [1, 2, 3, 4],
    'column3': [True, False, True, False],
    'column4': ['foo', 'foo', 'bar', 'bar']
})

# Better dtype inference using pandas
df['new_dtypes'] = df.apply(lambda x: x.dtypes, axis=1)

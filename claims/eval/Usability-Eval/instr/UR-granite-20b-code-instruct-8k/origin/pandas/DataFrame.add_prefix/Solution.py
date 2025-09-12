
import pandas as pd

# Create a Series
ser = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

# Prefix the row labels of the Series with 'row_'
prefixed_ser = ser.rename(lambda x: 'row_' + x)

# Create a DataFrame
df = pd.DataFrame({'col1': [4, 5, 6], 'col2': [7, 8, 9]}, index=['a', 'b', 'c'])

# Prefix the column labels of the DataFrame with 'col_'
prefixed_df = df.rename(columns=lambda x: 'col_' + x)

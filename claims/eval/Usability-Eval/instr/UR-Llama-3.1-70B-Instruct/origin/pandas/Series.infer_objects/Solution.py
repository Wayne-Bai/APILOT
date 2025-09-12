import pandas as pd
from io import StringIO

# create a sample dataframe
data = """
A,B,C
1,2,3
4,5,6
"""

# read the data into a dataframe, using the low_memory=False parameter
# to prevent pandas from attempting to infer dtypes automatically
df = pd.read_csv(StringIO(data), low_memory=False)

# iterate over the dataframe's columns
for col in df.columns:
    # check if the column is of dtype 'object'
    if df[col].dtype == 'object':
        # attempt to infer if the column can be safely converted to a more specific dtype
        try:
            # attempt to convert the column to numeric (int or float)
            df[col] = pd.to_numeric(df[col], errors='raise')
        except ValueError:
            # if the column cannot be converted to numeric, check if it can be converted to datetime
            try:
                df[col] = pd.to_datetime(df[col], errors='raise')
            except ValueError:
                # if the column cannot be converted to datetime, leave it as is
                pass

print(df.dtypes)

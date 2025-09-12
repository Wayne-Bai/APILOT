import pandas as pd

def last_non_null(df):
    return df.apply(lambda x: x.dropna().iloc[-1])

# Assuming `df` is your DataFrame
result = last_non_null(df)
print(result)

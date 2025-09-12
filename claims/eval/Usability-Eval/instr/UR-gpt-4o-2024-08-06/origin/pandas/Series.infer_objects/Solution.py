import pandas as pd

# Sample DataFrame with object columns
data = {
    'integers': ['1', '2', '3'],
    'floats': ['1.1', '2.2', '3.3'],
    'dates': ['2020-01-01', '2021-01-01', '2022-01-01'],
    'bools': ['True', 'False', 'True'],
    'strings': ['a', 'b', 'c']
}

df = pd.DataFrame(data)

# Function to infer better dtypes
def infer_better_dtypes(df):
    for column in df.select_dtypes(include='object').columns:
        try:
            df[column] = pd.to_numeric(df[column])
        except ValueError:
            try:
                df[column] = pd.to_datetime(df[column])
            except ValueError:
                if set(df[column].str.lower()).issubset({'true', 'false'}):
                    df[column] = df[column].str.lower() == 'true'
    return df

# Applying the function to infer better dtypes
df = infer_better_dtypes(df)

# Display the DataFrame with inferred dtypes
print(df)
print(df.dtypes)


import pandas as pd

# read in the data
df = pd.read_csv("data.csv")

# convert all object columns to categorical dtype
df = df.astype({col: "category" for col in df.columns if df[col].dtype == "object"})

# infer better dtypes for the remaining columns
df = pd.DataFrame(df)

# convert back to original data types
for col, dtype in df.dtypes.iteritems():
    if dtype == "category":
        df[col] = df[col].cat.codes

# save the converted dataframe as a new CSV file
df.to_csv("converted_data.csv", index=False)

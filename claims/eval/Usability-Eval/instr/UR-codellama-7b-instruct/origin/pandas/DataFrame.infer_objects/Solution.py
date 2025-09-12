
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Get a list of all object columns in the DataFrame
object_columns = df.select_dtypes(include=['object']).columns

# Infer better dtypes for each column by analyzing the data
for col in object_columns:
    inferred_type = pd.api.types.infer_dtype(df[col])
    if inferred_type == 'category':
        df[col] = df[col].astype('category')
    elif inferred_type == 'datetime64[ns]':
        df[col] = pd.to_datetime(df[col])

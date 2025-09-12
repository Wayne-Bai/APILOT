import pandas as pd

# Load your data into a pandas DataFrame
df = pd.read_csv("data.csv")

# Infer better data types for object columns
object_columns = df.select_dtypes(include=["object"])
inferred_dtypes = df[object_columns].apply(pd.infer_objects)
df[object_columns] = inferred_dtypes.astype("float")


import pandas as pd

# create a function to prefix labels with a string prefix
def prefix_labels(df, prefix):
    df.columns = [f"{prefix}{col}" for col in df.columns]
    return df

# example usage
df = pd.read_csv("data.csv")
prefixed_df = prefix_labels(df, "Prefix_")
print(prefixed_df)

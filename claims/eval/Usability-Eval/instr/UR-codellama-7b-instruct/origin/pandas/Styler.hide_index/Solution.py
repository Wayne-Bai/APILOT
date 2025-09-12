
import pandas as pd
df = pd.read_csv("data.csv")

# Drop a single column by label or number
df = df.drop(["age"], axis=1)

# Drop multiple columns using the drop() method
columns_to_drop = ["name", "id"]
df = df.drop(columns_to_drop, axis=1)

# Drop a range of columns using slicing
df = df.drop(range(2, 5), axis=1)

# Reset index to remove the dropped columns
df = df.reset_index()

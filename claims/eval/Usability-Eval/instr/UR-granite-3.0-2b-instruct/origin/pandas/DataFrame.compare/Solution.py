import pandas as pd

# Assuming df1 and df2 are your two DataFrames

# Check for differences in columns
diff_columns = df1.columns.difference(df2.columns)
print("Columns in df1 but not in df2: ", diff_columns)

# Check for differences in rows
diff_rows = df1[df1.duplicated(keep=False)] - df2[df2.duplicated(keep=False)]
print("Rows that are unique to df1: ")
print(diff_rows)

# Check for differences in values
diff_values = df1[df1.eq(df2)]
print("Rows where values are different: ")
print(diff_values)

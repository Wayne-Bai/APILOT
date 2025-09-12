import pandas as pd

# Assuming your data is stored in a DataFrame called "df"

# Pivot the first level of the hierarchical index
pivoted_df = df.reset_index().pivot(columns=["first_level_index"], values=["second_level_index"])

# Rename the columns to match the original DataFrame's format
pivoted_df.columns = [" ".join(col) for col in pivoted_df.columns]

print(pivoted_df)

import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to suffix
df['column_name_suffixed'] = df['column_name'].apply(lambda x: f"{x}_suffixed")

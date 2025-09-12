import pandas as pd

df = pd.read_csv('path_to_your_file.csv')
df['Group'] = pd.cut(df['numeric_column'], bins=quantiles, labels=False)
grouped_df = df.groupby('Group')['numeric_column'].quantile(q)

import pandas as pd

# Sample DataFrame
data = {
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Bangalore'],
    '2018': [100, 200, 300, 400],
    '2019': [150, 250, 350, 450]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Stack the prescribed level(s) from columns to index
df_stacked = df.melt(id_vars='City', value_vars=['2018', '2019'])

print("\nDataFrame after stacking:")
print(df_stacked)

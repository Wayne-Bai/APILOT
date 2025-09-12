import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to compute the sum of
df = pd.DataFrame({
    'column_name': [1, 2, 3, 4, 5]
})

# Compute the sum of 'column_name'
sum_of_group = df['column_name'].sum()

print(sum_of_group)

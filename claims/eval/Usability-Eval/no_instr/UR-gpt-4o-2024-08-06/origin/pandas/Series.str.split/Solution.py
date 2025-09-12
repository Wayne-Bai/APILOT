import pandas as pd

# Sample DataFrame
data = {'Column1': ['a_b_c', 'd_e_f', 'g_h_i']}
df = pd.DataFrame(data)

# Split the strings in 'Column1' around the underscore separator
split_df = df['Column1'].str.split('_', expand=True)

print(split_df)

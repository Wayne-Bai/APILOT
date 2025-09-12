import pandas as pd

# Sample DataFrame with strings to split
data = {'column_name': ['apple,banana,cherry', 'dog,cat', 'sun,moon,stars']}
df = pd.DataFrame(data)

# Split strings around a given separator (',') and expand into separate columns
df_expanded = df['column_name'].str.split(',', expand=True)

# Display the resulting DataFrame
print(df_expanded)

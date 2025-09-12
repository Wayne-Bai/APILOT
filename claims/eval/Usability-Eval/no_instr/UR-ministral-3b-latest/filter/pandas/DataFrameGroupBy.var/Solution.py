import pandas as pd

# Assuming you have a DataFrame `df` with a column ' 그룹' for groups and a column 'value' for the data to compute the variance on.
# This example also assumes there is a column 'value' with missing values represented as NaN

df = pd.read_csv('data.csv')

# Drop rows with missing values in the 'value' column
df = df.dropna(subset=['value'])

# Group by 'груп' (Wo should be the foreign name in German language, here I assumed English)
grouped = df.groupby('груп')

# Now compute the variance for each group
variance_by_group = grouped['value'].var()

print(variance_by_group)

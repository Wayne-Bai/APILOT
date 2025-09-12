import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Roll_Number': [1, 2, 3, 4],
    'Team': ['Team A', 'Team B', 'Team A', 'Team B']
}
df = pd.DataFrame(data)

# Pivot the DataFrame to stack levels from columns to index
stacked_df = df.set_index('Name').loc[:, ['Roll_Number', 'Team']]
print(stacked_df)

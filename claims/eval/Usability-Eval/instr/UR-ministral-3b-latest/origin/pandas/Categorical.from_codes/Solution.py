import pandas as pd

# Creating a dictionary of code categories.
code_categories = {'A': 'Alpha', 'B': 'Beta', 'C': 'Gamma', 'D': 'Delta', 'E': 'Epsilon'}

# Sample dataframe.
data = {'Code': ['A', 'B', 'C', 'D', 'E'], 'Value': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# Make the 'Code' column as a Categorical type with the created code categories.
df['Code'] = df['Code'].astype('category').cat.recode_object(code_categories, unknown=None, order=None, inplace=True)
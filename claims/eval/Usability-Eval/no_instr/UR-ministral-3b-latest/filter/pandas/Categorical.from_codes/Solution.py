import pandas as pd

# Assume we have two lists for codes and categories
codes = ['A', 'B', 'C', 'D', 'E']
categories = ['Inspi', 'Diving', ' Fighter', 'Sports', 'Football']

# Create a new DataFrame with the above lists
df = pd.DataFrame({'Code': codes, 'Category': categories})

# Convert 'Code' column to Categorical type
df['Code'] = pd.Categorical(df['Code'])

# Print the DataFrame to see the changes
print(df)

import pandas as pd

# Assuming df is your DataFrame and column is the name of your column
df = pd.DataFrame({'column': [True, 1, 'text', pd.Timestamp('20220101')]})

# Check if all elements in the column are Truthy
all_truthy = df['column'].all()
print(all_truthy)

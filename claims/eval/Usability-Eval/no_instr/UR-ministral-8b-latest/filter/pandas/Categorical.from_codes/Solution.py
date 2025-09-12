import pandas as pd

# Sample Data
data = {'code': ['A', 'B', 'A', 'B', 'C', 'B'],
        'category': ['first', 'second', 'first', 'second', 'third', 'second']}

# Create DataFrame
df = pd.DataFrame(data)

# Make a categorical type from codes and categories
df['category_code'] = pd.Categorical(df['category'], categories=['first', 'second', 'third'], ordered=True)

# Get the dtypes
print(df.dtypes)

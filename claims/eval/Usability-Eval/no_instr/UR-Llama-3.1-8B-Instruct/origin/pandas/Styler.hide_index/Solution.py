# Import the pandas library
import pandas as pd

# Create a sample DataFrame with an index
data = {
    'Company': ['ABC', 'DEF', 'GHI', 'JKL'],
    'Revenue': [100, 200, 300, 400],
    'Employees': [10, 20, 30, 40]
}
df = pd.DataFrame(data, index=['Q1', 'Q2', 'Q3', 'Q4'])

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Hide the entire index
print("\nHide the entire index:")
print(df.to_string(index=False))

# Hide specific keys in the index
print("\nHide specific keys in the index (Q2 and Q3):")
print(df.loc[df.index!= 'Q2'].loc[df.index!= 'Q3'].to_string(index=False))

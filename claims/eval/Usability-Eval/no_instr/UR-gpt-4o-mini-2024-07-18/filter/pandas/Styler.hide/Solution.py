import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Option 1: Hide entire index and column headers
print(df.to_string(index=False, header=False))

# Option 2: Hide specific columns by selecting only the desired columns
# Example: Hide column 'B'
print(df[['A', 'C']].to_string(index=False))

# Option 3: Hide specific rows by selecting only the desired rows
# Example: Hide the second row
print(df.drop(index=1).to_string(index=False))

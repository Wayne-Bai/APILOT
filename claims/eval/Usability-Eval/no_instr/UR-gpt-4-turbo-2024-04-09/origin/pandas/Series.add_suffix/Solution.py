import pandas as pd

# Sample DataFrame for demonstration
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Suffix the column labels with a string suffix
suffix = '_suffix'
df.columns = df.columns + suffix

print(df)

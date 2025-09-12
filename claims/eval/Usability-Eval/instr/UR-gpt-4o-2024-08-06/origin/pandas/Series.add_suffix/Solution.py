import pandas as pd

# Sample dataframe
data = {
    'column1': [1, 2, 3],
    'column2': [4, 5, 6],
    'column3': [7, 8, 9]
}
df = pd.DataFrame(data)

# Define the suffix
suffix = '_suffix'

# Add suffix to column labels
df.columns = [col + suffix for col in df.columns]

print(df)

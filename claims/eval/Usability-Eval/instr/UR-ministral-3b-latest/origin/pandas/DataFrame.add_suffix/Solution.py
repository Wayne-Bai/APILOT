import pandas as pd

# Example DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Define the string suffix
suffix = 'ylabel'

# Add suffix labels to each column
df.columns = [f'{col}_{suffix}' for col in df.columns]

print(df)

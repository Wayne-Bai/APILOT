import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'Age': ['25', '30', '35', '25', '30'],
    'Salary': ['50000', '60000', '70000', '50000', '60000'],
    'Department': ['HR', 'Engineering', 'HR', 'Engineering', 'HR']
}

# Create DataFrame
df = pd.DataFrame(data)

# Apply better dtypes to the columns
df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')
df['Salary'] = df['Salary'].apply(pd.to_numeric, errors='coerce')
df['Name'] = df['Name'].astype('category')

print(df.dtypes)

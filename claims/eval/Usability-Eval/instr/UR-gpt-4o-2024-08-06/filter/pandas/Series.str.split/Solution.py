import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown']}
df = pd.DataFrame(data)

# Split the 'Name' column into two separate columns: 'First Name' and 'Last Name'
df[['First Name', 'Last Name']] = df['Name'].str.split(' ', expand=True)

print(df)

import pandas as pd

# Sample data
data = {'Name': ['John Doe', 'Jane Smith', 'Bob Johnson']}
df = pd.DataFrame(data)

# Define the separator
separator = ' '

# Split the strings around the separator
df['First Name'] = df['Name'].str.split(separator, expand=True)[0]
df['Last Name'] = df['Name'].str.split(separator, expand=True)[1]

# Print the dataframe
print(df)

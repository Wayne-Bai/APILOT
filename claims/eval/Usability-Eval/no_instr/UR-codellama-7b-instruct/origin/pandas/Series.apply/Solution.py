
import pandas as pd

# Create a sample dataframe
data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 34, 45],
        'Gender': ['Male', 'Female', 'Male']}
df = pd.DataFrame(data)

# Create a new column based on the existing columns
df['New_Column'] = df['Name'].str.len() + df['Age']

# Print the new dataframe with the added column
print(df)

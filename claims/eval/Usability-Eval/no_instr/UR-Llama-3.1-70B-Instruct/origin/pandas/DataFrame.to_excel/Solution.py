# Importing necessary libraries
import pandas as pd

# Creating a dictionary containing some data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
}

# Converting the dictionary into DataFrame
df = pd.DataFrame(data)

# Writing DataFrame to an Excel sheet
df.to_excel('output.xlsx', index=False)

print("Data has been written to the Excel sheet successfully.")

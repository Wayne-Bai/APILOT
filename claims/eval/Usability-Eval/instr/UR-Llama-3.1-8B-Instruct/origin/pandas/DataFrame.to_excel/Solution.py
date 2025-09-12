# Import the pandas library and assign it the alias 'pd'
import pandas as pd

# Create a dictionary
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "Berlin", "London"]
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Create an ExcelWriter object
with pd.ExcelWriter('example.xlsx') as writer:
    # Write the DataFrame to the Excel file
    df.to_excel(writer, sheet_name='Sheet1', index=False)

print("Data has been written to the Excel file successfully.")

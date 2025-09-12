
import pandas as pd

# Create a dictionary to represent the data
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel("output.xlsx", index=False)

print("Data written to output.xlsx")

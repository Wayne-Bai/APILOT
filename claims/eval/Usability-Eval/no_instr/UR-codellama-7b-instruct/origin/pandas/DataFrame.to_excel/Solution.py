
import pandas as pd

# Create a sample dataframe
data = {'Name': ['John', 'Mary', 'David'], 'Age': [25, 31, 45], 'Gender': ['Male', 'Female', 'Other']}
df = pd.DataFrame(data)

# Write the dataframe to an Excel file
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer, index=False)
writer.save()

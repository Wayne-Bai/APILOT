import pandas as pd

# create a sample data frame
data = {'Name': ['John', 'Mary', 'David'],
        'Age': [23, 45, 67],
        'City': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

# write the data frame to an Excel file
with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1')

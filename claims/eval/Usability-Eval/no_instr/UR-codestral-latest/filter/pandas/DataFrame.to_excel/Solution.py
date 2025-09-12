# Import pandas library
import pandas as pd

# Data to be written to Excel
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 33],
    'City': ['New York', 'Paris', 'Berlin']
}

# Create DataFrame
df = pd.DataFrame(data)

# Write DataFrame to Excel
df.to_excel('output.xlsx', index = False)

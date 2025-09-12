# Import necessary libraries
import pandas as pd

# Create a sample DataFrame
data = {
    'Sales': [100, 200, 300, 400, 500],
    'Revenue': [2000, 6000, 10000, 12000, 15000]
}
df = pd.DataFrame(data)

# Suffix labels with a string suffix
df['Sales_Q1'] = df['Sales'].copy()
df['Revenue_Q1'] = df['Revenue'].copy()

pd.set_option('display.width', 100)
pd.set_option('display.max.columns', None)

# Print the updated DataFrame
print(df)

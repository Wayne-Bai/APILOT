import pandas as pd

# Sample DataFrame
data = {'column1': [1, '', None, 'Text', False],
        'column2': [None, 0, 'Data', False, 'True'],
        'column3': ['Value1', 'Value2', '', 'Value4', 0]}

df = pd.DataFrame(data)

# Function to check if any element in the DataFrame is Truthy
def any_element_Truthy(df):
    return df.astype(str).values.astype(bool).any().any()

if any_element_Truthy(df):
    print("There is at least one Truthy element in the DataFrame.")
else:
    print("All elements in the DataFrame are Falsy.")

# Import pandas library
import pandas as pd

# Function to split strings around a given separator
def split_strings(data, column_name, separator):
    # Create a new DataFrame with the split strings
    df = pd.DataFrame(data)
    df = df.assign(**{column_name: df[column_name].str.split(separator, expand=True)})
    
    return df

# Create a DataFrame
data = {'Strings': ['hello,world', 'python,pandas', 'ai,machine,learning'],
        'OtherColumn': [1, 2, 3]}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Split the 'Strings' column around the comma separator
df = split_strings(df, 'Strings', ',')

print("\nDataFrame after splitting strings:")
print(df)

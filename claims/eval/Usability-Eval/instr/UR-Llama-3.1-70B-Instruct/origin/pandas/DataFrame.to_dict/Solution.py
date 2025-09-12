# Import the pandas library
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Convert the DataFrame to a dictionary
dict_from_df = df.to_dict(orient='records')

# Print the dictionary
for i, item in enumerate(dict_from_df):
    print(f"Row {i+1}: {item}")

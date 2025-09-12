# Import pandas
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame:")
print(df)

# Convert the DataFrame to a dictionary
df_dict = df.to_dict(orient='records')

# Print the dictionary
print("\nDictionary:")
print(df_dict)

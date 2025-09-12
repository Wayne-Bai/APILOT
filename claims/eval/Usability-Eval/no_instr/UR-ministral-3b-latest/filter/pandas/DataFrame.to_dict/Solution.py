import pandas as pd

# Create DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 35],
    'City': ['New York', 'Paris', 'Berlin']
}
df = pd.DataFrame(data)

# Convert DataFrame to a dictionary
df_dict = df.to_dict(orient='dict')

print(df_dict)

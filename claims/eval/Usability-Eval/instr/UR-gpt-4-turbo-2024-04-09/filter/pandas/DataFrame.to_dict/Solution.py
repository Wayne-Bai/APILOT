import pandas as pd

# Example DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# Convert the DataFrame to a dictionary
result_dict = df.to_dict(orient='records')
print(result_dict)

import pandas as pd

# Sample JSON string
json_string = '''
{
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "SQL", "Data Analysis"]
}
'''

# Convert JSON string to pandas DataFrame
df = pd.read_json(json_string, orient='index').T

# Display the DataFrame
print(df)

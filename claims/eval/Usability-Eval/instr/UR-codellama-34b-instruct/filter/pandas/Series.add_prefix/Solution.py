import pandas as pd

# sample data
data = {'name': ['John', 'Jane', 'Sam', 'Amy'],
        'age': [20, 30, 40, 50],
        'city': ['New York', 'Paris', 'Tokyo', 'London']}
df = pd.DataFrame(data)

# prefix label with string "label_"
df['label_name'] = df['name'].str.lower()
df['label_age'] = df['age'].astype('string') + '_years'
df['label_city'] = df['city'].str.upper()

print(df)

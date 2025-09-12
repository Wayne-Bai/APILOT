import pandas as pd

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [23, 56, 78, 45],
        'Country': ['USA', 'UK', 'Canada', 'Australia']}

df = pd.DataFrame(data)

df['Prefix'] = 'Mr.'

print(df)


import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [23, 56, 78, 34]}
df = pd.DataFrame(data)
index_array = df.index.values
print(index_array)

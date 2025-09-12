import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Female', 'Male', 'Non Binary']}
df = pd.DataFrame(data)
print(df.reset_index())
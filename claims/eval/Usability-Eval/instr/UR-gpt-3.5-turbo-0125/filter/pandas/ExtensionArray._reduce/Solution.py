
import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)

result = df['A'].sum()

print(result)

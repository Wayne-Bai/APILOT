
import pandas as pd

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 3, 4, 5, 6],
    'C': [3, 4, 5, 6, None],
    'D': [4, 5, 6, None, None]
}

df = pd.DataFrame(data)

correlation_matrix = df.corr()
print(correlation_matrix)

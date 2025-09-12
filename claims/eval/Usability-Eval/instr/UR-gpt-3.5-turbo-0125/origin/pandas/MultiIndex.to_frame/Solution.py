
import pandas as pd

data = {
    ('A', 'first'): [1, 4, 7],
    ('A', 'second'): [2, 5, 8],
    ('B', 'first'): [3, 6, 9],
    ('B', 'second'): [10, 11, 12]
}

df = pd.DataFrame(data)

print(df)

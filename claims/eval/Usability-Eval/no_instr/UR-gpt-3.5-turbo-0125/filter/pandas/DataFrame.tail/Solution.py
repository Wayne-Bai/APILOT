
import pandas as pd

# create a sample dataframe
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# return the last n rows (for example n=2)
n = 2
last_n_rows = df.tail(n)
print(last_n_rows)

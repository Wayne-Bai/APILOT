import pandas as pd

# Example DataFrame
data = {
    'A': ['foo', 'bar', 'foo', 'bar'],
    'B': [1, 2, 3, 4],
    'C': [5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Stack the specified level(s) from columns to index
result = df.stack()
print(result)

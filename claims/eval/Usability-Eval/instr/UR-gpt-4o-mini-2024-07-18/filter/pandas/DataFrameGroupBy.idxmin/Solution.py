import pandas as pd

def first_index_of_min(df, axis=0):
    return df.apply(lambda x: x.idxmin() if len(x) > 0 else None, axis=axis)

# Example usage:
data = {
    'A': [1, 2, None, 4],
    'B': [4, 3, 2, None],
    'C': [None, 1, 0, 1]
}
df = pd.DataFrame(data)

result = first_index_of_min(df, axis=0)
print(result)

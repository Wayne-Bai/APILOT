import pandas as pd

def return_quantile(df, quantile, axis):
    return df.quantile(quantile, axis=axis)

# Example usage:
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
}

df = pd.DataFrame(data)

print(return_quantile(df, 0.5, 0))
print(return_quantile(df, 0.5, 1))

import pandas as pd

def check_truthy(series):
    return series.apply(lambda x: bool(x)).any()

# Example usage:
data = {'col1': [1, 2, 3], 'col2': [True, False, None], 'col3': ['a', 'b', 'c']}
df = pd.DataFrame(data)
print(check_truthy(df['col1']))  # True
print(check_truthy(df['col2']))  # True
print(check_truthy(df['col3']))  # True

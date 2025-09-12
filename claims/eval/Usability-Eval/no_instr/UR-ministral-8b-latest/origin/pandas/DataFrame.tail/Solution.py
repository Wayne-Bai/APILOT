import pandas as pd

# Sample data for demonstration
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': ['foo', 'bar', 'baz', 'qux', 'corge', 'grault', 'garply', 'waldo', 'fred', 'plugh']
}
df = pd.DataFrame(data)

def get_last_n_rows(df, n):
    return df.tail(n)

# Example usage
last_5_rows = get_last_n_rows(df, 5)
print(last_5_rows)

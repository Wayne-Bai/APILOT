import pandas as pd

def check_truthiness(df, column_name):
    return df[column_name].any().any()

# Example usage
df = pd.DataFrame({
    'A': [0, 0, 1, 0],
    'B': [0, 1, 0, 0]
})
print(check_truthiness(df, 'A'))  # Output: False
print(check_truthiness(df, 'B'))  # Output: True

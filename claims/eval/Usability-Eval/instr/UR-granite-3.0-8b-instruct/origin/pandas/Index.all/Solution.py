import pandas as pd

def check_all_truthy(df):
    return df.applymap(bool).all().all()

# Example usage:
data = {'A': [True, False, True], 'B': [True, True, True]}
df = pd.DataFrame(data)
print(check_all_truthy(df))  # Output: True

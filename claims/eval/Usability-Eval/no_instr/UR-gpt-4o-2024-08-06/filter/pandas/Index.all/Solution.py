import pandas as pd

# Sample DataFrame
data = {
    'A': [True, 1, 'non-empty string'],
    'B': [False, 0, ''],
    'C': [True, 2, 'another string']
}

df = pd.DataFrame(data)

# Check if all elements in the DataFrame are truthy
def check_all_truthy(df):
    return df.all().all()

# Usage
are_all_truthy = check_all_truthy(df)
print("Are all elements truthy?:", are_all_truthy)

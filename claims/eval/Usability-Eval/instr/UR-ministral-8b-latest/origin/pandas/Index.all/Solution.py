import pandas as pd

def check_all_truthy(df):
    # Check if all elements in the DataFrame are Truthy
    return (df == df).all().all()

# Example usage:
data = {'A': [True, False, True], 'B': [1, 2, 3], 'C': [None, None, None]}
df = pd.DataFrame(data)

result = check_all_truthy(df)
print(result)  # Output: False

data_truthy = {'A': [True, True, True], 'B': [1, 2, 3], 'C': [1, 2, 3]}
df_truthy = pd.DataFrame(data_truthy)

result_truthy = check_all_truthy(df_truthy)
print(result_truthy)  # Output: True

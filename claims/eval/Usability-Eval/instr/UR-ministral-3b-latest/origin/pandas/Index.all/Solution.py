import pandas as pd

# Example DataFrame
data = {'A': [True, False, True, False], 'B': [True, True, False, True]}
df = pd.DataFrame(data)

# Define a function to check if all elements are Truthy
def all_elements_truish(df):
    return all(df.applymap(lambda x: x is True).all())

# Check for all elements in the DataFrame
print(all_elements_truish(df))

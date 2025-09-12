# Importing the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'A': [True, True, False, False],
    'B': [1, 2, '', None],
    'C': [True, False, True, False],
    'D': [1, 2, '', None]
}
df = pd.DataFrame(data)

# Checking if all elements are truthy
def check_truthy(df):
    # Use the DataFrame's all() method with apply(pd.to_numeric, errors='coerce') and compare to a list of true values
    for col in df:
        if df[col].apply(lambda x: pd.to_numeric(x, errors='coerce').notnull()).all():
            print(f"All elements in column {col} are truthy.")
        else:
            print(f"Not all elements in column {col} are truthy.")

check_truthy(df)

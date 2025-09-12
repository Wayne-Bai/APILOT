import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to check
def check_truthiness(df, column_name):
    return df[column_name].astype(bool).any()

# Example usage:
# df = pd.DataFrame({'A': [True, False, True], 'B': [False, False, False]})
# print(check_truthiness(df, 'A'))  # Returns True
# print(check_truthiness(df, 'B'))  # Returns False

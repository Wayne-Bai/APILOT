import pandas as pd

def check_truthy_elements(df):
    return any(df.applymap(lambda x: x).values)

# Example Usage
data = {'Column1': [0, 1, None, '','False', False, '', True],
        'Column2': [0, False, '', 1, None, 'True', 'True', False]}
df = pd.DataFrame(data)

print(check_truthy_elements(df))

import pandas as pd

def all_truthy(data):
    return all(data)

data = pd.DataFrame({'col1': [True, True], 'col2': [False, True], 'col3': [True, False]})
result = all_truthy(data)
print(result)

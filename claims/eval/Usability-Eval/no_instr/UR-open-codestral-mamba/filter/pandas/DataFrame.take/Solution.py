import pandas as pd

def get_elements(dataframe, indices):
    return dataframe.iloc[indices]

# Test the function
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)
indices = [0, 2]  # Desired indices
print(get_elements(df, indices))

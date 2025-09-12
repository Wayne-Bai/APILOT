
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]}

df = pd.DataFrame(data)

# Function to return elements at specified positional indices along axis
def get_elements(df, axis, indices):
    if axis == 0:
        result = df.iloc[indices]
    elif axis == 1:
        result = df.iloc[:, indices]
    return result

# Specify axis and positional indices
axis = 0  # 0 for rows, 1 for columns
indices = [1, 3]  # Positional indices to select

# Call the function to get elements at specified indices
selected_elements = get_elements(df, axis, indices)
print(selected_elements)

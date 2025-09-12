import pandas as pd

# Function to check if all elements in a DataFrame or Series are Truthy
def all_elements_truthy(data):
    return data.astype(bool).all()

# Example usage with a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

result = all_elements_truthy(df)
print(result)  # Output: True

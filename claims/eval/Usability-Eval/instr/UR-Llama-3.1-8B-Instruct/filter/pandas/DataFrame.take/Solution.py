import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Return the elements in the given positional indices along an axis
def get_elements(df, indices, axis):
    try:
        return df.loc[indices, df.columns if axis == 0 else index]
    except (KeyError, IndexError):
        return "Invalid index or axis"

# Example usage
indices = [0, 2]
axis = 0

result = get_elements(df, indices, axis)
print("\nElements at position", indices, "along axis", axis, ":", result)

indices = [1, 3]
axis = 1

result = get_elements(df, indices, axis)
print("\nElements at position", indices, "along axis", axis, ":", result)

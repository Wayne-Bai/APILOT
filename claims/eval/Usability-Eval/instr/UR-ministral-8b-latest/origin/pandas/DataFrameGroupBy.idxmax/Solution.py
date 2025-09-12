import pandas as pd

def index_of_first_max(arr, axis=0):
    max_index = arr.idxmax(axis=axis)
    max_idx = max_index[0] if isinstance(max_index, pd.Series) else max_index
    return max_idx

# Example usage:
data = pd.DataFrame({
    'A': [1, 5, 3, 2],
    'B': [7, 1, 9, 5]
})

index = index_of_first_max(data["A"], axis=0)
print(f"The index of the first occurrence of maximum in A is: {index}")

index = index_of_first_max(data[["A", "B"]], axis=1)
print(f"The index of the first occurrence of maximum in columns A and B is: {index}")

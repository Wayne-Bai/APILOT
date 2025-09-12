import pandas as pd

def index_of_first_minimum(arr, axis=0):
    # Create a mask for non-NA/null values
    mask = pd.notna(arr)

    if axis == 0:
        first_min_idx = mask[arr].idxmin().min()
    else:
        first_min_idx = mask[arr.T].idxmin().min()

    if first_min_idx is None:
        raise ValueError("No valid index found")

    return first_min_idx

# Example usage:
data = pd.DataFrame({
    'A': [3, 7, 5, 2],
    'B': [2, 4, 9, None],
    'C': [1, 3, 7, 8]
})

print(index_of_first_minimum(data, axis=0))  # Output: 3
print(index_of_first_minimum(data, axis=1))  # Output: 0

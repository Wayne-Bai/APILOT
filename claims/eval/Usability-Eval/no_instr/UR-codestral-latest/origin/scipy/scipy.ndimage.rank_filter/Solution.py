import numpy as np

def rank_filter(data, window_size):
    # Create an empty array to hold the rank filtered data
    rank_filtered_data = np.zeros_like(data)

    # Get the shape of the data
    shape = data.shape

    # Calculate the window radius
    radius = window_size // 2

    # Iterate over each dimension of the data
    for i in range(data.ndim):
        # Create a new axis indexing array
        new_axis_idx = [np.newaxis] * i + [slice(None)] + [np.newaxis] * (data.ndim - i - 1)

        # Iterate over each point in the data
        for j in range(shape[i]):
            # Calculate the start and end indices of the window
            start = max(0, j - radius)
            end = min(shape[i], j + radius + 1)

            # Extract the window of data and rank it
            window = data[new_axis_idx[:i] + [slice(start, end)] + new_axis_idx[i+1:]]
            ranked_window = np.apply_along_axis(lambda x: np.rank(x, method='min'), i, window)

            # Place the ranked window back into the rank filtered data
            rank_filtered_data[new_axis_idx[:i] + [j] + new_axis_idx[i+1:]] = ranked_window[new_axis_idx[:i] + [radius if start <= j < end else (j-start)] + new_axis_idx[i+1:]]

    return rank_filtered_data

# Example usage:
data = np.array([[1, 9, 2], [8, 3, 7], [4, 6, 5]])
window_size = 3
print(rank_filter(data, window_size))

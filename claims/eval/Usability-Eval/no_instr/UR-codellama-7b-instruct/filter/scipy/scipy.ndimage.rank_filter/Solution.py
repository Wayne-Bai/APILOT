
import scipy.ndimage as ndi

# Define the array to be filtered
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Apply a multidimensional rank filter with window size (3, 3) and threshold of 0.5
rank_filtered = ndi.rank_filter(data, np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]]), 0.5)

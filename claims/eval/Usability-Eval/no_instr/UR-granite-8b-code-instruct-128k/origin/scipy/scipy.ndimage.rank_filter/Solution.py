import scipy.ndimage as ndi
# Define the input array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Define the kernel size
kernel_size = 3
# Apply the rank filter
output = ndi.rank_filter(arr, rank=kernel_size)

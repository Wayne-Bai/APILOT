
from scipy import stats

# Define a multidimensional array
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculate the percentile filter
percentile_filter = stats.mstats.mquantiles(data, prob=[0.1, 0.2, 0.3])

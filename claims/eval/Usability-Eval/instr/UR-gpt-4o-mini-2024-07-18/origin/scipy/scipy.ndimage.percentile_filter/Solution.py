import numpy as np
from scipy.ndimage import percentile_filter

def apply_percentile_filter(data, percentile, footprint=None):
    """
    Apply a multidimensional percentile filter to the data.

    Parameters:
    - data: ndarray, input data to be filtered
    - percentile: float, the percentile value to compute
    - footprint: ndarray, optional, defines the neighborhood for the filter

    Returns:
    - filtered_data: ndarray, the result of the percentile filter
    """
    filtered_data = percentile_filter(data, percentile, footprint=footprint)
    return filtered_data

# Example usage
if __name__ == "__main__":
    # Create sample data
    sample_data = np.random.rand(5, 5)
    print("Original Data:\n", sample_data)

    # Apply the percentile filter
    result = apply_percentile_filter(sample_data, 50)  # 50th percentile (median)
    print("Filtered Data (50th Percentile):\n", result)

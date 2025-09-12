
import numpy as np
from scipy import stats

def calculate_percentile_filter(data, percentiles):
    # Calculate the percentiles of the data
    percentiles = stats.scoreatpercentile(data, percentiles)
    
    # Create a mask for the filtered data
    mask = np.zeros((len(data),))
    for i in range(len(percentiles)):
        mask[i] = (data[:,i] >= percentiles[i])
        
    # Return the filtered data
    return data[mask]


import numpy as np
from scipy import stats

def calculate_relative_z_scores(data):
    # Calculate the mean and standard deviation of the data
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    
    # Calculate the relative z-scores for each data point
    relative_z_scores = (data - mean) / std
    
    return relative_z_scores

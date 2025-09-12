import scipy

def compute_coefficient_of_variation(data):
    mean = scipy.mean(data)
    std_dev = scipy.std(data)
    coefficient_of_variation = std_dev / mean
    return coefficient_of_variation
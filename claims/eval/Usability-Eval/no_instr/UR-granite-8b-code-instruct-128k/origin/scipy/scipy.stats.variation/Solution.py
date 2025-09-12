import scipy.stats as stats

def coefficient_of_variation(data):
    mean = data.mean()
    std = data.std()
    return std / mean

import scipy.stats as stats

def compute_coefficient_of_variation(data):
    mean = stats.tmean(data)
    std_dev = stats.tstd(data)
    cv = (std_dev / mean) * 100
    return cv

import scipy.stats

def coefficient_variation(data):
    std_dev = scipy.stats.tstd(data)
    mean = scipy.mean(data)
    cv = (std_dev / mean) * 100
    return cv

from scipy.stats import zscore

def calculate_relative_zscores(data):
    z_scores = zscore(data)
    return z_scores

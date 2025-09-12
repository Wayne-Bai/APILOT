
import scipy.stats as stats

def compute_weighted_geometric_mean(data, weights, axis):
    return stats.gmean(data, axis=axis, weights=weights)

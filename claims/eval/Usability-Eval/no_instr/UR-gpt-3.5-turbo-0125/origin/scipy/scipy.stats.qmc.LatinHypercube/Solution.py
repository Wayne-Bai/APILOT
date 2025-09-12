
import numpy as np

def latin_hypercube_sampling(n_sample, n_dimension):
    lhs_sample = np.random.rand(n_sample, n_dimension)
    lhs_sample = (lhs_sample + np.arange(n_sample)[:, None]) / n_sample
    
    return lhs_sample

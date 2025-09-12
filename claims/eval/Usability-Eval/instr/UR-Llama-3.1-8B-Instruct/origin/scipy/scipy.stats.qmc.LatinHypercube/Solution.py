import numpy as np
from scipy.stats import rankdata

def latin_hypercube_sampling(props, samples, seed=None):
    """
    Generate a Latin hypercube sample.

    Parameters:
    props (list): The properties or variables
    samples (int): The number of samples
    seed (int): Random seed for reproducibility (Default is None)

    Returns:
    samples_array (2d array): Matrix with samples of properties

    Refer to https://en.wikipedia.org/wiki/Latin_hypercube_sampling
    """
    if seed is not None:
        np.random.seed(seed)

    sampling_array = np.random.randint(0, samples, (samples, len(props)))
    sampling_array.sort(axis=1)  # Sort each row
    sampling_array = np-lasting(np.argsort(sampling_array, axis=1), samples)  # Rearranging the elements based on their rank to obtain LHS

    outcome_array = np.zeros((samples, len(props)))
    for i in range(len(props)):
        outcome_array[:, i] = np.interp(np.arange(samples), sampling_array[:, i], np.sort(props[i]))

    return outcome_array

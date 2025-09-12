import numpy as np
from scipy.stats import qmc

def generate_scrambled_sobol(dimensions, samples):
    # Generate Sobol' sequence
    sampler = qmc.Sobol(d=dimensions, scramble=False)
    sequence = sampler.random_base2(m=samples)

    # Apply random permutation to scramble the sequence
    idx = np.random.permutation(samples)
    sequence = sequence[idx, :]

    return sequence

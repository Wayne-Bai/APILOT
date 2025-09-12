import scipy.stats
import numpy as np

def scrambled_sobol_sequence(dimensions, samples):
    # Create a Sobol' sequence generator with scrambling
    sobol_gen = scipy.stats.qmc.Sobol(d=dimensions, scramble=True)
    
    # Generate the samples
    sample = sobol_gen.random_base2(m=int(np.log2(samples)))
    
    return sample

# Define the number of dimensions and samples
dim = 5
num_samples = 32  # Must be a power of two when using random_base2

# Generate the sequence
sequence = scrambled_sobol_sequence(dim, num_samples)
print("Scrambled Sobol' Sequence:")
print(sequence)

import numpy as np
from scipy.special import comb

def generate_sobol_sequence(n, dim, scramble=False):
    if scramble:
        # Scramble the sequence using a random permutation
        permutation = np.random.permutation(n)
        return np.array([sequence[i] for i in permutation])
    else:
        # Generate the Sobol' sequence
        sequence = np.zeros((n, dim))
        for i in range(dim):
            sequence[:, i] = np.floor((np.arange(n) + 0.5) / (2 ** i)) % 2
        return sequence

def generate_sobol_sequences(n, dim, num_sequences, scramble=False):
    sequences = []
    for _ in range(num_sequences):
        sequences.append(generate_sobol_sequence(n, dim, scramble))
    return np.array(sequences)

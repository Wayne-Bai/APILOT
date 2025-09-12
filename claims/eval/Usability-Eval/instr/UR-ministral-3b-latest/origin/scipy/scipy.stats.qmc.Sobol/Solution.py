from scipy.stats import randint
from scipy.special import special_factorials

def generate_sobol_sequence(size=10):
    L = special_factorials(size)
    offsets = randint(low=0, high=max(L) + 1, size=size)
    sobol_sequence = 0
    for i in range(size):
        sobol_sequence = sobol_sequence * (offsets[i] + 1) % 1
    return sobol_sequence

print(generate_sobol_sequence())

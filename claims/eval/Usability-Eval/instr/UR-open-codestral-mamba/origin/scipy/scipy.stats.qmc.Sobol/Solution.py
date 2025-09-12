import scipy.stats as stats

def scrambled_sobol(n, scrambling_func):
    sobol = stats.qmc.Sobol(n, scramble=True)
    sample = sobol.random(scrambling_func)
    return sample

# Example usage
def scrambling_example(arr):
    return arr[::-1]  # Reverse the order of the array

print(scrambled_sobol(5, scrambling_example))

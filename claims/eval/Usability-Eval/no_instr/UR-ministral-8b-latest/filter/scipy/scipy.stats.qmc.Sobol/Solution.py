from scipy.stats import qmc

def generate_sobol_sequences(dim, n_samples):
    sobol_gens = qmc.Sobol(n=dim)
    samples = sobol_gens.random(n=n_samples)
    scrambled_sobol = sobol_gens.random(n=n_samples)
    return scrambled_sobol

# Example usage:
dim = 3
n_samples = 100
scrambled_sobol_samples = generate_sobol_sequences(dim, n_samples)

import scipy.stats.qmc as qmc

def generate_scrambled_sobol(dimensions, samples):
    # Create a Sobol' sequence generator object with scrambling
    sobol_gen = qmc.Sobol(d=dimensions, scramble=True)

    # Generate the required number of samples
    sobol_samples = sobol_gen.random(n=samples)

    return sobol_samples

# Example usage: generating a 5-dimensional Sobol' sequence of 100 samples
sobol_data = generate_scrambled_sobol(5, 100)
print(sobol_data)

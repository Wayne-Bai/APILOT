import numpy as np

# Drawing samples from a uniform distribution between 0 and 1
samples = np.random.default_rng().uniform(low=0.0, high=1.0, size=10)
print(samples)

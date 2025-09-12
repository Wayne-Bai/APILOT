import numpy as np

# Draw samples from a uniform distribution between 0 and 1
uniform_samples = np.random.uniform(0, 1, 10)

print("Uniform distribution samples: ", uniform_samples)

# Draw samples from a uniform distribution between 1 and 10
uniform_samples_1_10 = np.random.uniform(1, 10, 10)

print("Uniform distribution samples between 1 and 10: ", uniform_samples_1_10)

# Draw samples from a uniform distribution between -10 and 10
uniform_samples_neg10_10 = np.random.uniform(-10, 10, 10)

print("Uniform distribution samples between -10 and 10: ", uniform_samples_neg10_10)

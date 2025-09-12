import numpy as np

# Generate a single sample from a uniform distribution ranging from 0 to 1
single_sample = np.random.uniform(0, 1)
print(f'Single sample: {single_sample}')

# Generate multiple samples from a uniform distribution ranging from 0 to 1
size = (2, 3)  # 2*3 matrix
multiple_samples = np.random.uniform(0, 1, size)
print(f'Multiple samples:\n{multiple_samples}')

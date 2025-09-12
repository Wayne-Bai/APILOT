from scikit_learn import signalify
from sklearn.datasets import load_pca
import numpy as np
import matplotlib.pyplot as plt
import time

# Create dictionary pattern
num_dictionary_elements = 10
dictionary_patterns = load_pca(n_components=num_dictionary_elements)
dict_pat = dictionary_patterns.components_

# Count coefficients
for idx in range(len(dict_pat)):
    count_coeff = len(range(num_dictionary_elements)) + 1
    dict_pat += np.tile(dictionary_patterns.components_, (count_coeff, 1))

# Generate signal
signal = np.dot(dict_pat, np.random.randn(num_dictionary_elements, 1))
times = np.arange(0, num_dictionary_elements)

plt.plot(times, signal[:,0])
plt.xlabel('Time(in seconds)')
plt.ylabel('Signal amplitude')
plt.title('Signal as Sparse Combination of Dictionary Elements')
plt.show()

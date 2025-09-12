from sklearn.decomposition import MiniBatchSparsePCA
import numpy as np

# Define the dictionary elements
dictionary = np.random.rand(100, 1000)  # 100 elements, each of size 1000

# Generate a sparse signal
n_samples = 1000
n_features = 1000
alpha = 0.1  # sparsity level
signal = np.zeros(n_features)
indices = np.random.choice(n_features, size=int(n_features * alpha), replace=False)
signal[indices] = np.random.rand(len(indices))

# Apply MiniBatchSparsePCA to recover the signal
mb_spca = MiniBatchSparsePCA(n_components=10, alpha=0.1, batch_size=100, random_state=42)
recovered_signal = mb_spca.fit_transform(dictionary, signal)

print("Original signal:", signal[:10])
print("Recovered signal:", recovered_signal[:10])

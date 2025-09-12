from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.datasets import make_data
from sklearn.pipeline import make_pipeline

# Generate example data
X, _ = make_data(n_samples=100, n_features=20, random_state=42)

# Create the dictionary learning pipeline
model = make_pipeline(
    MiniBatchDictionaryLearning(n_components=8, max_iter=10, random_state=42),
    MiniBatchDictionaryLearning(n_components=8, max_iter=10, random_state=42)
)

# Fit the model
model.fit(X, X)

# Get the learned atoms
atoms = model.named_steps['mldl-0'].atoms_

print("Learned atoms:")
print(atoms)

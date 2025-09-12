
from sklearn.linear_model import OrthogonalMatchingPursuit

# Generate a signal as a sparse combination of dictionary elements
D = np.random.rand(10, 5)
X = OrthogonalMatchingPursuit(n_components=3).fit_transform(D)
Y = D @ X

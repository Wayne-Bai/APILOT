from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import make_classification

# Generate a random dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Initialize the GaussianNB model
gnb = GaussianNB()

# Perform online updates to model parameters via partial_fit
for i in range(10):
    gnb.partial_fit(X[i*100:(i+1)*100], y[i*100:(i+1)*100], classes=np.unique(y))

# Print the model parameters
print(gnb.theta_)
print(gnb.sigma_)

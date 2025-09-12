
from sklearn.datasets import make_classification
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.inspection import plot_partial_dependence

# Generate a random binary classification problem
X, y = make_classification(n_samples=1000, n_features=5,
 n_informative=3, n_redundant=0, random_state=0,
 shuffle=False)

# Create a GradientBoostingClassifier instance
gb = GradientBoostingClassifier(n_estimators=100, random_state=0)

# Train the classifier
gb.fit(X, y)

# Compute the partial dependence plot for a single feature
plot_partial_dependence(gb, X, [0])

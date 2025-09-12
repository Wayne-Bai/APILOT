from sklearn.inspection import plot_partial_dependence
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Create a logistic regression estimator
clf = LogisticRegression()

# Plot the partial dependence of the first feature (sepal length)
plot_partial_dependence(clf, X, [0], response_method='predict_proba')

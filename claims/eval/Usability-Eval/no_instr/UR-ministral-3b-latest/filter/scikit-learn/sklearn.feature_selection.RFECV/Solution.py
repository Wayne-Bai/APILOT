from sklearn.feature_selection import RFECV
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load dataset
iris = load_iris()

# Initialize the logistic regression model
logreg = LogisticRegression(max_iter=200)

# Initialize RFECV
rfe = RFECV(logreg, 10, step=1, cv=5)

# Fit RFECV
rfe.fit(iris.data, iris.target)

# Get the selected number of features
selected_features = rfe.n_features_

# Get the support vectors
selected_features_indices = rfe.support_

print(f'Selected features: {selected_features_indices}')
print(f'Selected features number: {selected_features}')

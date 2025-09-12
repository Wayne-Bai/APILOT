from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Set up RFECV
selector = RFECV(estimator=LogisticRegression(), cv=5, step=1)
selector.fit(X, y)

# Get selected features
selected_features = selector.support_

# Print the number of features selected
print('Selected features:', sum(selected_features))

# Train and predict using the selected features
selected_X = selector.transform(X)
clf = LogisticRegression()
clf.fit(selected_X, y)

# Predict on new data
# new_data = ...
# new_predictions = clf.predict(new_data)

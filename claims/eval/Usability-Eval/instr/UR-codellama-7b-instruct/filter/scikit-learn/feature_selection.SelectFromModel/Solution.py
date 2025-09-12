
from sklearn.feature_selection import SelectKBest

# Import the data set
X = ... # feature matrix
y = ... # target vector

# Create a select K best feature selector
selector = SelectKBest(k=10)

# Fit the selector to the data
selector.fit(X, y)

# Get the selected features and their importance scores
selected_features = selector.get_support()
importance_scores = selector.scores_

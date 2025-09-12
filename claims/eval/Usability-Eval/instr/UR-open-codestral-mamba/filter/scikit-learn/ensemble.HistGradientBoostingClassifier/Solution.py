from sklearn.ensemble import HistGradientBoostingClassifier

# Sample data
X = [[1, 2], [3, 4], [5, 6]]
y = [1, 0, 1]

# Create a Histogram-based Gradient Boosting Classifier
hgb = HistGradientBoostingClassifier(max_iter=100)

# Train the model
hgb.fit(X, y)

# Predict the outcome for some new data
output = hgb.predict(X)
print(output)

import sklearn
from sklearn.experimental import enable_hist_gradient_boosting  # noqa
from sklearn.ensemble import HistGradientBoostingClassifier

# Example data
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load data
data = load_iris()
X, y = data.data, data.target

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a histogram-based gradient boosting classifier
model = HistGradientBoostingClassifier()

# Train the model using the training data
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

print(predictions)

from sklearn.experimental import enable_hist_gradient_boosting  # noqa
from sklearn.ensemble import HistGradientBoostingClassifier

# Instantiate the model
hgb_classifier = HistGradientBoostingClassifier()

# Example data
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load iris dataset and split it
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
hgb_classifier.fit(X_train, y_train)

# Predicting the test set results
y_pred = hgb_classifier.predict(X_test)

# Evaluating the results
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

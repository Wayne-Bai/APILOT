from sklearn.calibration import CalibratedClassifierCV
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model on the training data
clf = CalibratedClassifierCV(base_estimator=LogisticRegression(), cv=5, method="sigmoid")
clf.fit(X_train, y_train)

# Predict probabilities on the test set
predictions = clf.predict_proba(X_test)

# Compute true and predicted probabilities for a calibration curve
true_probs = predictions[:, 1]
predicted_probs = clf.classes_[predictions].ravel()

# Plot the calibration curve
plt.plot([0, 1], [0, 1], 'k--')
plt.scatter(true_probs, predicted_probs)
plt.xlabel('True Probability')
plt.ylabel('Predicted Probability')
plt.show()

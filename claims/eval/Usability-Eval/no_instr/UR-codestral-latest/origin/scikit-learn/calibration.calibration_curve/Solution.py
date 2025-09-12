from sklearn.calibration import calibration_curve
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Create a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression classifier
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Compute predicted probabilities
y_pred_prob = clf.predict_proba(X_test)[:, 1]

# Compute true and predicted probabilities for a calibration curve
fraction_of_positives, mean_predicted_value = calibration_curve(y_test, y_pred_prob, n_bins=10)

print(f'Fraction of positives: {fraction_of_positives}')
print(f'Mean predicted value: {mean_predicted_value}')

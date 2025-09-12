from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

# Generate a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

# Calibrate the probabilities using isotonic regression
calibrated_lr = CalibratedClassifierCV(lr, cv='prefit', method='isotonic')
calibrated_lr.fit(X_train, y_train)

# Make predictions using the calibrated model
y_pred_prob = calibrated_lr.predict_proba(X_test)[:, 1]

# Evaluate the performance of the calibrated model
y_pred = calibrated_lr.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("AUC-ROC:", roc_auc_score(y_test, y_pred_prob))

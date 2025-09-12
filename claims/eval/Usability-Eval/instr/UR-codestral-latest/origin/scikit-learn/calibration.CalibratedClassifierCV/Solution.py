from sklearn.isotonic import IsotonicRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Create a random binary classification problem
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit the classifier
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Get predicted probabilities for the validation set
y_val_pred_prob = clf.predict_proba(X_val)[:, 1]

# Fit the calibrator
calibrator = IsotonicRegression(out_of_bounds='clip')
calibrator.fit(y_val_pred_prob, y_val)

# Calibrate the predictions
y_val_calibrated_prob = calibrator.transform(y_val_pred_prob)

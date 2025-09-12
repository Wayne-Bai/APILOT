import numpy as np
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.calibration import CalibratedClassifierCV

# Generate some random data
X = np.random.rand(100, 10)
y = np.random.randint(0, 2, size=100)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a calibration object for isotonic regression
iso_cal = IsotonicRegression()

# Fit the model on the training data
iso_cal.fit(X_train, y_train)

# Predict probabilities for the testing data
y_pred_iso = iso_cal.predict(X_test)

# Create a calibration object for logistic regression
log_cal = LogisticRegression()

# Fit the model on the training data
log_cal.fit(X_train, y_train)

# Predict probabilities for the testing data
y_pred_log = log_cal.predict(X_test)

# Compute calibration error for both models
iso_err = np.mean((y_pred_iso - y_test)**2)
log_err = np.mean((y_pred_log - y_test)**2)

print("Isotonic regression calibration error:", iso_err)
print("Logistic regression calibration error:", log_err)

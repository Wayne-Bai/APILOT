# Import necessary libraries
from sklearn.calibration import CalibratedClassifierCV
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the iris dataset
data = load_iris()
X, y = data.data, data.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Create a logistic regression model
lr = LogisticRegression()

# Train the model
lr.fit(X_train, y_train)

# Create a calibrated model using isotonic regression
calibrated_lr = CalibratedClassifierCV(lr, cv='prefit', method='isotonic')

# Fit the calibrated model
calibrated_lr.fit(X_train, y_train)

# Display the score of the calibrated model
print("Isotonic calibration score: ", calibrated_lr.score(X_test, y_test))

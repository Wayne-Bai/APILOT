from sklearn.isotonic import IsotonicRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# Create a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict probabilities for the test set
y_pred = model.predict_proba(X_test)[:, 1]

# Fit isotonic regression on the predicted and true values
calibrator = IsotonicRegression(out_of_bounds='clip')
calibrator.fit(y_pred, y_test)

# Transform the predicted probabilities to be more reliable
calibrated_y_pred = calibrator.transform(y_pred)


from sklearn.linear_model import LogisticRegression

# Create an instance of the LogisticRegression class
logreg = LogisticRegression()

# Fit the model to your data
logreg.fit(X, y)

# Make predictions on new data
predictions = logreg.predict(X_new)

# Import necessary libraries
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import HistGradientBoostingClassifier

# Create a test dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, random_state=42)

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the HistGradientBoostingClassifier
hgbc = HistGradientBoostingClassifier(random_state=42)

# Fit the model to the training data
hgbc.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = hgbc.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred))

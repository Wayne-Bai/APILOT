from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc

# Load the iris dataset
data = load_iris()
X = data.data
y = data.target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a RandomForestClassifier model
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_score = clf.predict_proba(X_test)

# Compute the ROC curve and ROC area for manually using the ROC protocol
fpr, tpr, _ = roc_curve(y_test, y_score.ravel())
roc_auc = auc(fpr, tpr)

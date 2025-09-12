# Import necessary libraries
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve, auc, average_precision_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt

# Generate a random dataset for binary classification
X, y = make_classification(n_samples=10000, n_features=20, n_informative=5, n_redundant=3, n_repeated=0, n_classes=2, random_state=42)

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a classifier
classifier = RandomForestClassifier(random_state=42)
classifier.set_params(n_estimators=100)
classifier.fit(X_train, y_train)

# Predict on test set
y_pred_proba = classifier.predict_proba(X_test)[:, 1]

# Label binarize y_test for multiclass
y_test_binarized = label_binarize(y_test, classes=[0, 1])

# Plot precision recall curve
precision, recall, thresholds = precision_recall_curve(y_test_binarized.flatten(), y_pred_proba)
auc_score = auc(recall, precision)

plt.figure(figsize=(8,6))
plt.plot(recall, precision, marker='.', label=f'AUC-PR = {auc_score:.4f}')

# Plot average precision score
avg_precision = average_precision_score(y_test_binarized, y_pred_proba)
plt.title("Precision Recall Curve - AUC-PR: {:.4f}, AP: {:.4f}".format(auc_score, avg_precision))
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.legend()
plt.show()

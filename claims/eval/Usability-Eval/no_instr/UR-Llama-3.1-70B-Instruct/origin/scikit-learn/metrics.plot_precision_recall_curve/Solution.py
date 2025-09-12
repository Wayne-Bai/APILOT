# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import precision_recall_curve, auc, average_precision_score
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
import numpy as np

# Generate a random binary classification dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=3, n_classes=2, n_clusters_per_class=1, random_state=42)

# Split the dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a binary classifier (Logistic Regression in this case)
clf = LogisticRegression(max_iter=10000)
clf.fit(X_train, y_train)

# Predict probabilities for the test set
y_pred_prob = clf.predict_proba(X_test)[:,1]

# Calculate precision and recall
precision, recall, _ = precision_recall_curve(y_test, y_pred_prob)

# Calculate the Area Under the Precision Recall Curve (AUPRC)
auprc = auc(recall, precision)

# Calculate the Average Precision (AP) score
ap = average_precision_score(y_test, y_pred_prob)

# Print out the AUPRC and AP score
print(f"AUPRC: {auprc:.2f}")
print(f"AP score: {ap:.2f}")

# Plot the Precision Recall Curve
plt.figure(figsize=(8, 6))
plt.plot(recall, precision, marker='.', label=f'Precision Recall Curve (AUPRC = {auprc:.2f})')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision Recall Curve')
plt.legend()
plt.show()

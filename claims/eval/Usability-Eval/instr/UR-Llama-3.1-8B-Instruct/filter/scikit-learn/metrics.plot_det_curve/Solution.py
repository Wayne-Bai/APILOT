# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_circles
from sklearn.tree import DecisionTreeClassifier  # Using a decision tree classifier for simplicity
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import numpy as np

# Generate a sample dataset
X, y = make_circles(n_samples=200, factor=.2, noise=.05, random_state=0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Standardize features by removing the mean and scaling to unit variance
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

# Train a Decision Tree Classifier model
clf = DecisionTreeClassifier(random_state=0)
clf = clf.fit(X_train_std, y_train)

# Get predictions on the test set
y_pred = clf.predict(X_test_std)

# Calculate the true positives, false positives, false negatives, and true negatives
TN, FP, FN, TP = confusion_matrix(y_test, y_pred).ravel()

# Calculate the true positive rate and the false positive rate at each threshold
fpr, tpr, _ = roc_curve(y_test, clf.predict_proba(X_test_std)[:, 1])

# Calculate the AUC (the rate at which the model correctly identifies positive examples)
auc_value = auc(fpr, tpr)

# Plot the Receiver Operating Characteristic (ROC) curve
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (AUC = %0.2f)' % auc_value)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

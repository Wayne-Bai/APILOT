import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

# Load the data and split it into features and labels
X = ...  # feature matrix
y = ...  # label vector

# Create a random forest classifier
clf = RandomForestClassifier()

# Train the classifier on the training data
clf.fit(X, y)

# Predict probabilities for the test data
probabilities = clf.predict_proba(X)

# Compute the ROC curve and AUC score
fpr, tpr, thresholds = roc_curve(y, probabilities[:, 1])
auc = roc_auc_score(y, probabilities[:, 1])

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for Random Forest Classifier')
plt.legend(loc="lower right")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, auc
import matplotlib.pyplot as plt

# Assuming X is the features and y is the target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a binary classifier
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Predict probabilities
y_score = clf.predict_proba(X_test)[:, 1]

# Calculate precision and recall
precision, recall, _ = precision_recall_curve(y_test, y_score)

# Calculate the area under the curve (AUC)
auc_pr = auc(recall, precision)

# Plot the precision-recall curve
plt.plot(recall, precision, label='Precision-Recall curve (area = {:%.2f})'.format(auc_pr))
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc="lower right")
plt.show()

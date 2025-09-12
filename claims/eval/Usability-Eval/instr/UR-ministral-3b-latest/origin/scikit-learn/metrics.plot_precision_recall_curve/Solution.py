import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc
from sklearn.datasets import make_classification
from sklearn.preprocessing import label_binarize
from sklearn import svc

# Create a binary classification dataset
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Example binary classification model
model = svc.SVC(kernel='linear', probability=True)

# Fit the model on the training data
model.fit(X_train, y_train)

# Predict the probability scores of the test set
y_proba = model.predict_proba(X_test)

# Get the precision and recall
precision, recall, thresholds = precision_recall_curve(y_test, y_proba[:, 1])

# Compute the area under the precision-recall curve
precision_recall_area = auc(recall, precision)

# Plot precision-recall curve
plt.figure()
plt.plot(recall, precision, label='Precision-Recall curve')
plt.title('Precision-Recall Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.legend()
plt.grid(True)
plt.show()

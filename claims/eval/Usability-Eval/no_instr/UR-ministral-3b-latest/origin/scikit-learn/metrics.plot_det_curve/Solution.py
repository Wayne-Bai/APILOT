import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import numpy as np
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
X = data.data[:, :2]
y = (data.target == 0).astype(int)

# Initialize model and forecast
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X, y)

# Predict probabilities
probs = model.predict_proba(X)[:, 1]

# Calculate ROC Curve and AUC
fpr, tpr, thresholds = roc_curve(y, probs)
roc_auc = auc(fpr, tpr)

# Plotting
plt.plot(fpr, tpr, color='darkorange', label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

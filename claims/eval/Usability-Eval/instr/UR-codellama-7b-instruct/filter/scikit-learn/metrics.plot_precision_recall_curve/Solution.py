import numpy as np
from sklearn import metrics
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Generate random dataset
X = np.random.rand(100, 2)
y = (np.sum(X, axis=1) > 0.5).astype(int)

# Plot Precision Recall Curve for binary classifier
precision, recall, thresholds = metrics.precision_recall_curve(y, probas_pred=None)
pr_auc = auc(recall, precision)
plt.plot(recall, precision, label='Precision-Recall curve')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='upper left')
plt.show()

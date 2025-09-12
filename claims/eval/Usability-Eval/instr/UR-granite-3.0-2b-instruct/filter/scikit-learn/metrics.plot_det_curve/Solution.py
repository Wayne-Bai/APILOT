from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import numpy as np

# Assume y_true and y_score are your true labels and predicted probabilities respectively
y_true = np.array([0, 0, 1, 1, 1, 0, 1, 1, 0, 1])
y_score = np.array([0.1, 0.4, 0.35, 0.8, 0.6, 0.5, 0.9, 0.7, 0.2, 0.5])

# Calculate false positive rate and true positive rate
fpr, tpr, thresholds = roc_curve(y_true, y_score)

# Calculate area under the curve
roc_auc = auc(fpr, tpr)

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()

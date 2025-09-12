import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, average_precision_score

# Example binary classifier predictions and true labels
y_true = np.array([0, 1, 1, 0, 1, 0, 1, 0, 0, 1])
y_scores = np.array([0.1, 0.4, 0.35, 0.8, 0.7, 0.2, 0.9, 0.3, 0.6, 0.5])

# Compute precision-recall pairs for different probability thresholds
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)

# Compute average precision score
average_precision = average_precision_score(y_true, y_scores)

# Plot the precision-recall curve
plt.figure()
plt.step(recall, precision, color='b', alpha=0.2, where='post')
plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title(f'Precision-Recall curve: AP={average_precision:.2f}')
plt.show()

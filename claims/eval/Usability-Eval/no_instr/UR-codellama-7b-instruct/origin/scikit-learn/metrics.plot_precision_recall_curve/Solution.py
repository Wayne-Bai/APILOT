import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

# Generate some random data
y_true = np.array([0, 1, 2, 3])
y_pred = np.array([0.1, 0.4, 0.35, 0.8])

# Compute precision recall curve
precision, recall, _ = metrics.precision_recall_curve(y_true, y_pred)

# Plot the curve
plt.plot(recall, precision)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.show()

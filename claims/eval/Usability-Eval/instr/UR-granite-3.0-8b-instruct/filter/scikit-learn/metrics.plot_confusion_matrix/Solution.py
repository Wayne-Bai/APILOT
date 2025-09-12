from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import matplotlib.pyplot as plt

# Assume y_true and y_pred are your true and predicted labels
y_true = np.array([2, 0, 2, 2, 0, 1, 1, 2, 2, 0])
y_pred = np.array([0, 1, 2, 2, 0, 2, 1, 2, 2, 2])

# Create confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Plot confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1, 2])
disp.plot(cmap=plt.cm.Blues)
plt.show()

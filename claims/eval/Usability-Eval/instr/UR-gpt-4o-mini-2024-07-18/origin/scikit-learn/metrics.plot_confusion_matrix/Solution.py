import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Example data
y_true = np.array([0, 1, 0, 1, 0, 1, 1, 0])  # True labels
y_pred = np.array([0, 0, 1, 1, 0, 1, 0, 1])  # Predicted labels

# Calculate confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Create confusion matrix display
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[0, 1])

# Plot the confusion matrix
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

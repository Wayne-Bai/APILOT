
import numpy as np
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt

# Generate some dummy data for demonstration purposes
y_true = [1, 0, 0, 1, 0, 1, 1, 0, 1]
y_pred = [1, 1, 0, 0, 1, 0, 0, 1, 1]

# Create a confusion matrix using the true and predicted values
conf_mat = confusion_matrix(y_true, y_pred)

# Plot the confusion matrix as an image
plt.figure(figsize=(6, 6))
sns.heatmap(conf_mat, annot=True, fmt=".2f", cmap="Blues")
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.show()

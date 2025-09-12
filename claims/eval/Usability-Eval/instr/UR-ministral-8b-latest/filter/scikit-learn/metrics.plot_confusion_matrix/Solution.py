import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Generate some dummy data for the purpose of this example
y_true = np.array([0, 1, 2, 2, 1])
y_pred = np.array([0, 0, 2, 1, 1])

# Compute the confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Plot the confusion matrix
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.colorbar()
tick_marks = np.arange(len(np.unique(y_true)))
plt.xticks(tick_marks, np.unique(y_true))
plt.yticks(tick_marks, np.unique(y_true))

plt.ylabel('True label')
plt.xlabel('Predicted label')

# Add the count of predictions to the cells
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center", color="red")

plt.show()

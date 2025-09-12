
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
# Example confusion matrix
y_true = np.array(['cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog'])
y_pred = np.array(['cat', 'cat', 'dog', 'dog', 'cat', 'dog', 'cat', 'dog'])
# Create confusion matrix
cm = confusion_matrix(y_true, y_pred)
# Plot confusion matrix
plt.matshow(cm)
plt.colorbar()
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

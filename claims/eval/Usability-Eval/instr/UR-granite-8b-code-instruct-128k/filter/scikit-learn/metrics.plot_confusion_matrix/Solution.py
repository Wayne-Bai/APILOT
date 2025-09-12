from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
y_true = [2, 0, 2, 2, 0, 1, 1, 2, 2, 1, 1, 2, 0, 2, 1, 0]
y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 0, 1, 2, 1, 0]
cm = confusion_matrix(y_true, y_pred)
plt.imshow(cm, interpolation='nearest')
plt.colorbar()
tick_marks = np.arange(3)
plt.xticks(tick_marks, ['Class 0', 'Class 1', 'Class 2'])
plt.yticks(tick_marks, ['Class 0', 'Class 1', 'Class 2'])
plt.title('Confusion matrix')
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()

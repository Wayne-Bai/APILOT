import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Example usage:
# Assuming 'y_true' and 'y_pred' are the true labels and predicted labels respectively
y_true = [0, 1, 2, 1, 0]
y_pred = [0, 0, 2, 1, 0]

conf_matrix = confusion_matrix(y_true, y_pred)

plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()

plt.ylabel('True label')
plt.xlabel('Predicted label')
tick_marks = [0, 1, 2]
plt.xticks(tick_marks, [0, 1, 2])
plt.yticks(tick_marks, [0, 1, 2])

plt.show()

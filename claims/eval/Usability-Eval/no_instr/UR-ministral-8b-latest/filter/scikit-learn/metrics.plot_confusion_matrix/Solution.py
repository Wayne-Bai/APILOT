import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Assuming you have a validation data Aragument:
# true_labels, predicted_labels:
true_labels = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
predicted_labels = [0, 0, 0, 1, 1, 0, 1, 1, 0, 1]

# Create a confusion matrix
cm = confusion_matrix(true_labels, predicted_labels)

# Plot the confusion matrix using seaborn
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.show()

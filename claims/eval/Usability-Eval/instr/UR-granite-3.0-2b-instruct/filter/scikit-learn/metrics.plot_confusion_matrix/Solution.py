from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming y_true and y_pred are your true and predicted labels
cm = confusion_matrix(y_true, y_pred)

# Normalize the confusion matrix
cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

# Plot the confusion matrix
plt.figure(figsize=(10, 7))
sns.heatmap(cm_norm, annot=True, fmt=".2f", cmap="Blues")
plt.xlabel('Predicted label')
plt.ylabel('True label')
plt.show()

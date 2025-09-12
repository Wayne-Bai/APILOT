from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

# Assume y_true and y_score are your true labels and predicted probabilities respectively
precision, recall, thresholds = precision_recall_curve(y_true, y_score)

# Plot the precision-recall curve
plt.plot(recall, precision, label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall curve')
plt.legend()
plt.show()

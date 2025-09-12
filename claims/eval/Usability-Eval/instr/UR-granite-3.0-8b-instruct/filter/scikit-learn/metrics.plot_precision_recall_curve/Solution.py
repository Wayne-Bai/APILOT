from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

# Assuming y_true and y_score are your true labels and predicted probabilities
precision, recall, _ = precision_recall_curve(y_true, y_score)

plt.step(recall, precision, color='b', alpha=0.2, where='post')
plt.fill_between(recall, precision, alpha=0.2, color='b')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.show()

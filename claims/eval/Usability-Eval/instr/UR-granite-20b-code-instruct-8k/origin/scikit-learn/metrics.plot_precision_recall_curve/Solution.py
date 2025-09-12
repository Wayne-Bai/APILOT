from sklearn.metrics import precision_recall_curve

y_true = ...  # True labels of the test set
y_score = ...  # Probabilities of the positive class

precision, recall, thresholds = precision_recall_curve(y_true, y_score)

# Plot the precision-recall curve
import matplotlib.pyplot as plt

plt.plot(recall, precision, label="Precision-Recall curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.legend()
plt.show()

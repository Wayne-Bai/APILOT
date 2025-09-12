from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt

# Assuming y_true, y_pred_proba are defined for the binary classifier
y_true = ...
y_pred_proba = ...

precision, recall, thresholds = precision_recall_curve(y_true, y_pred_proba)

plt.plot(recall, precision, marker='.')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.show()

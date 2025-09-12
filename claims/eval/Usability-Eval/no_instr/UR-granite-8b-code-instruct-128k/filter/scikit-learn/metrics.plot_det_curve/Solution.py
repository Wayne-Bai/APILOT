from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

y_true = [0, 0, 1, 1]
y_scores = [0.1, 0.4, 0.35, 0.8]

# Calculate ROC curve and AUC
roc_curve_values = roc_curve(y_true, y_scores)
roc_auc = auc(roc_curve_values[0], roc_curve_values[1])

# Plot ROC curve
plt.figure()
plt.plot(roc_curve_values[0], roc_curve_values[1], color='darkorange',
         label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

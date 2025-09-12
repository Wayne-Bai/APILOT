import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, average_precision_score

# Assuming y_true and y_score are already defined
# y_true: true labels
# y_score: predicted scores

precision, recall, thresholds = precision_recall_curve(y_true, y_score)
average_precision = average_precision_score(y_true, y_score)

plt.figure()
plt.plot(recall, precision, 'b-', label='PR curve')
plt.title('Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.legend(loc='best')
plt.grid(True)
plt.show()

print('Average Precision:', average_precision)

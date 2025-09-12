import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc

# Import some data to play with
X = datasets.load_iris().data
y = datasets.load_iris().target

# Run classifier
classifier = svm.SVC(kernel='linear', probability=True)
classifier.fit(X, y)

# Plot ROC curve
y_score = classifier.decision_function(X)

false_positive_rate, true_positive_rate, thresholds = roc_curve(y, y_score)
roc_auc = auc(false_positive_rate, true_positive_rate)

plt.figure()
lw = 2  # Line width
plt.plot(false_positive_rate, true_positive_rate, color='darkorange', lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')  # Random classification (AUC = 0.5)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

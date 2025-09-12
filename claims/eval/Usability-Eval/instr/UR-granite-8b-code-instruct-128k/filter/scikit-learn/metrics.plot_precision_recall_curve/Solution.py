from sklearn import datasets
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import plot_precision_recall_curve
import matplotlib.pyplot as plt

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Plot Precision-Recall Curve
precision, recall, thresholds = precision_recall_curve(y, X[:, 2])
plot_precision_recall_curve(precision, recall, thresholds)
plt.show()

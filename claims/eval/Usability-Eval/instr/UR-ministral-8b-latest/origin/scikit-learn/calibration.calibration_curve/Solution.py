import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc

# Sample data
X, y = np.arange(100).reshape((-1, 1)), np.random.randint(0, 2, 100)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Fit a Gaussian Process Classifier
gpc = GaussianProcessClassifier()
gpc.fit(X_train, y_train)

# Predict probabilities
y_score = gpc.predict_proba(X_test)

# Calculate true and predicted probabilities
true_labels = y_test
predicted_labels = np.round(gpc.predict(X_test)).astype(int)

# Calculate the calibration curve
bin_boundaries = np.linspace(0, 1, num=10)
mapping = {0: 'low risk', 1: 'high risk'}

binched_probabilities = []
binched_labels = []

for bin_edge in bin_boundaries:
    filtered_probabilities = y_score[:, np.where(y_score[:,1] >= bin_edge)[0]]
    filtered_labels = y_test[np.where(y_score[:, 1] >= bin_edge)[0]]

    binched_probabilities.append(filtered_probabilities)
    binched_labels.append(filtered_labels)

bin_boundaries = np.concatenate(([0], bin_boundaries, [1]))

# Plotting calibration curve
plt.figure(figsize=(10, 8))
for bin_prob, bin_label in zip(binched_probabilities, binched_labels):
    proportions = np.bincount(bin_label)
    proportions = proportions / proportions.sum()
    plt.plot(bin_boundaries[:-1], proportions, label=str(bin_boundaries[:-1])[:-1])

# Show plot
plt.xlabel("Calibrated Probability")
plt.ylabel("Criteria")
plt.title("Calibration Curve")

plt.legend()
plt.grid(True)
plt.show()

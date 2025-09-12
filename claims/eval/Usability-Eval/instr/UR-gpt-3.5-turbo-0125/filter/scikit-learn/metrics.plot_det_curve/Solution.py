
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have the true labels y_true and predicted probabilities y_scores

# Calculate ROC curve
def calculate_roc_curve(y_true, y_scores):
    n = len(y_scores)
    thresholds = np.unique(y_scores)
    thresholds = np.insert(thresholds, 0, thresholds[0] - 1)
    tpr_list = []
    fpr_list = []

    for threshold in thresholds:
        y_pred = (y_scores >= threshold).astype(int)
        tp = np.sum((y_true == 1) & (y_pred == 1))
        fp = np.sum((y_true == 0) & (y_pred == 1))
        tn = np.sum((y_true == 0) & (y_pred == 0))
        fn = np.sum((y_true == 1) & (y_pred == 0))

        tpr = tp / (tp + fn)
        fpr = fp / (fp + tn)
        tpr_list.append(tpr)
        fpr_list.append(fpr)

    return np.array(fpr_list), np.array(tpr_list)

# Plot ROC curve
def plot_roc_curve(y_true, y_scores):
    fpr, tpr = calculate_roc_curve(y_true, y_scores)
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.show()

# Example usage
y_true = np.array([0, 1, 0, 1, 1])
y_scores = np.array([0.1, 0.4, 0.3, 0.8, 0.7])
plot_roc_curve(y_true, y_scores)

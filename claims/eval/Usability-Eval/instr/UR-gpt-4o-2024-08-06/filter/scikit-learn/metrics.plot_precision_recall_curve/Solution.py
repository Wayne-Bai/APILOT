import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# Creating a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Splitting the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initializing and training the model
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

# Predicting probabilities
y_scores = model.decision_function(X_test)

# Calculating precision and recall
precisions, recalls, thresholds = precision_recall_curve(y_test, y_scores)

# Calculating the area under the precision-recall curve
pr_auc = auc(recalls, precisions)

# Plotting the Precision-Recall curve
plt.figure(figsize=(8, 6))
plt.plot(recalls, precisions, label=f'AUC = {pr_auc:.2f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc='best')
plt.grid()
plt.show()

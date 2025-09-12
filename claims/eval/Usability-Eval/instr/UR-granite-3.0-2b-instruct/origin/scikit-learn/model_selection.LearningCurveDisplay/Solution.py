from sklearn.model_selection import learning_curve
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Assume X and y are your features and target variable
svm = SVC()
train_sizes, train_scores, test_scores = learning_curve(svm, X, y, cv=5)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

plt.figure()
plt.grid()

plt.fill_between(train_sizes, train_mean-train_std, train_mean+train_std, alpha=0.1, color="r")
plt.fill_between(train_sizes, test_mean-test_std, test_mean+test_std, alpha=0.1, color="g")
plt.plot(train_sizes, train_mean, 'o-', color="r", label="Training score")
plt.plot(train_sizes, test_mean, 'o-', color="g", label="Cross-validation score")

plt.legend(loc="best")
plt.show()
